import random

from lib.generator import generator
from lib.lemmatizer import lemmatizer
from lib.tokenizer import sentences
from lib.types import *


class CorrectionPreposition:
    def __init__(self):
        syllables = generator.get_syllables()
        self.prep = syllables[random.randrange(len(syllables))]

    def __str__(self):
        return '"{} " + word'.format(self.prep)

    def apply(self, base_word: str) -> str:
        return self.prep + ' ' + base_word


class CorrectionSuffix:
    def __init__(self):
        syllables = generator.get_syllables()
        self.suffix = syllables[random.randrange(len(syllables))]

    def __str__(self):
        return 'word + "{}"'.format(self.suffix)

    def apply(self, base_word: str) -> str:
        return base_word + self.suffix


class CorrectionNone:
    def apply(self, base_word: str) -> str:
        return base_word

    def __str__(self):
        return 'word as is'


CORRECTIONS = [CorrectionPreposition, CorrectionSuffix]


class Language:
    def __init__(self, generator):
        self.generator = generator
        self.dictionary = {}  # word_base_eng => Word(word_base, gender)
        self.grammar = {}  # Trait(gender, countable) => correction
        for p in PARTS:
            for g in GENDERS:
                for c in COUNTABLE:
                    trait = Trait(part=p, gender=g, countable=c)
                    non_corrected_part = p in (ARTICLE, PREPOSITION, None)
                    correction = CorrectionNone() if non_corrected_part else random.choice(CORRECTIONS)()
                    self.grammar[trait] = correction

    def get_alphabet(self):
        return self.generator.get_alphabet()

    def generate_root(self, word_eng_base, part, letter=None) -> str:
        if word_eng_base in self.dictionary:
            return self.dictionary[word_eng_base].word_base
        while True:
            new_root = self.generator.gen_root(word_eng_base, part)
            if letter is not None:
                new_root = letter + new_root
            if new_root in (word.word_base for _, word in self.dictionary.items()):
                continue
            return new_root

    def generate_root_for_abc(self, word_eng_base, letter=None) -> (int, str, int):
        countable, part, eng_word_base = lemmatizer.get_countable_and_base(word_eng_base)
        new_word_base = self.generate_root(word_eng_base, part, letter)
        new_gender = random.choice(GENDERS)
        return part, new_word_base, new_gender, countable, eng_word_base

    def correct_word(self, eng_word_base, part, countable, gender=None):
        word = self.dictionary.get(eng_word_base)
        if word is None:
            return None
        g = gender if gender is not None else word.gender
        correction = self.grammar[Trait(part=part, gender=g, countable=countable)]
        return correction.apply(word.word_base)

    def translate_abc_word(self, letter: str, eng_words: list) -> str:
        eng_word = eng_words.pop(0)
        new_part, new_word_base, new_gender, new_countable, eng_word_base = self.generate_root_for_abc(eng_word, letter)
        word = Word(part=new_part, word_base=new_word_base, gender=new_gender)
        self.dictionary[eng_word_base] = word
        correction = self.grammar[Trait(part=word.part, gender=word.gender, countable=new_countable)]
        return correction.apply(word.word_base), eng_word_base

    def translate_word_token(self, token: Token) -> str:
        # countable     from    text
        # word          from    genetaor
        # correction    from    grammar

        if token.word_base in self.dictionary:
            word = self.dictionary[token.word_base]
        else:
            new_gender = random.choice(GENDERS)
            new_word_base = self.generate_root(token.word_base, token.part)
            word = Word(part=token.part, word_base=new_word_base, gender=new_gender)
            self.dictionary[token.word_base] = word

        correction = self.grammar[Trait(part=word.part, gender=word.gender, countable=token.countable)]
        return correction.apply(word.word_base)

    def translate_token(self, token: Token) -> str:
        if token.type == 'WORD':
            new_word = self.translate_word_token(token)
            if token.value.isupper():
                new_word = new_word.upper()
            elif token.value.istitle():
                new_word = new_word.title()
            return new_word
        else:
            return token.value

    def translate(self, text):
        result = []
        for token_sentence in sentences(text):
            # todo: base word countable
            sentence = []
            for token in token_sentence:
                sentence.append(self.translate_token(token))
            result.append(''.join(sentence))
        return ''.join(result)


def print_dictionary_word(lang, means, word, singular):
    result = []
    if word.part is not None:
        if word.part == NOUN:
            result.append(
                '{:<10} ({}, {}, pl.: {}) means: {}'.format(
                    singular.title(),
                    PARTS_NAMES[word.part].title(),
                    GENDERS_NAMES[word.gender].title(),
                    lang.correct_word(means, word.part, PLURAL).title(),
                    means.title()
                ),
            )
        else:
            variants = []
            if word.part in (ADJECTIVE, VERB):
                ranges = [
                    (NEUTER, SINGULAR),
                    (FEMALE, SINGULAR),
                    (FEMALE, PLURAL),
                    (MALE, PLURAL),
                ]
                for g, c in ranges:
                    range_variant = lang.correct_word(means, word.part, c, g)
                    if range_variant == singular:
                        continue
                    variants.append(
                        '{} ({} {})'.format(
                            range_variant,
                            GENDERS_NAMES_SHORT[g],
                            COUNTABLE_NAMES[c]
                        )
                    )
            result.append(
                '{:<10} ({}) means: {}'.format(
                    singular.title(),
                    PARTS_NAMES[word.part].title(),
                    means.title()
                ),
            )
            if variants:
                result.append(' ' * 10 + ' ' + ', '.join(variants))
    else:
        result.append(
            '{:<10} means: {}'.format(
                singular.title(),
                means.title()
            )
        )

    return "\n".join(result)


def print_dictionary(lang: Language) -> str:
    result = []
    items = ((k, v, lang.correct_word(k, v.part, SINGULAR)) for k, v in lang.dictionary.items())
    for means, word, singular in sorted(items, key=lambda t: t[2]):
        result.append(print_dictionary_word(lang, means, word, singular))
        result.append('')

    return "\n".join(result)


def print_grammar(lang: Language):
    result = []
    for p in PARTS:
        result.append(PARTS_NAMES[p])
        for g in GENDERS:
            t_single = Trait(part=p, gender=g, countable=SINGULAR)
            t_plural = Trait(part=p, gender=g, countable=PLURAL)
            result.append('{:<10} singular: {:<20} plural: {:<20}'.format(
                GENDERS_NAMES[g],
                str(lang.grammar[t_single]),
                str(lang.grammar[t_plural])
            ))
        result.append('')
    return "\n".join(result)


def print_abc(lang: Language, alphabet: str, alphabet_words: list):
    result = []
    for letter in list(alphabet):
        new_word, eng_word_base = lang.translate_abc_word(letter, alphabet_words)
        word = lang.dictionary[eng_word_base]
        singular = lang.correct_word(eng_word_base, word.part, SINGULAR)

        result.append('[ {} ]'.format(letter.upper()))
        result.append(print_dictionary_word(lang, eng_word_base, word, singular))
        result.append('')

    return "\n".join(result)
