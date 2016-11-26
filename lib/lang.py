import random

from lib.generator import Generator
from lib.tokenizer import Token
from lib.types import *

generator = Generator()


class CorrectionPreposition:
    def __init__(self, trait: Trait):
        syllables = generator.get_syllables()
        self.prep = syllables[random.randrange(len(syllables))]

    def apply(self, base_word: str) -> str:
        return self.prep + ' ' + base_word

    def __str__(self):
        return '"{}" + _ + word'.format(self.prep)


class CorrectionSuffix:
    def __init__(self, suffix):
        syllables = generator.get_syllables()
        self.suffix = syllables[random.randrange(len(syllables))]

    def apply(self, base_word: str) -> str:
        return base_word + self.suffix

    def __str__(self):
        return 'word + "{}"'.format(self.suffix)


CORRECTIONS = [CorrectionPreposition, CorrectionSuffix]


def determine_text_word(text_word: str) -> (int, str):
    # word_eng_countable, word_eng_part, word_eng_base = lemmatizer.get_countable_and_base(text_word)
    return word_eng_countable, word_eng_base


def generate_new_word(word_eng_base: str):
    return generator.gen_root(word_eng_base)
    # return gen(word_eng_base)


class Language:
    def __init__(self, seed):
        self.dictionary = {}  # word_base_eng => Word(word_base, gender)
        self.grammar = {}  # Trait(gender, countable) => correction
        for g in GENDERS:
            for c in COUNTABLE:
                trait = Trait(gender=g, countable=c)
                self.grammar[Trait(gender=g, countable=c)] = random.choice(CORRECTIONS)(trait)

                # self.grammar = {
                #     Trait(gender=NEUTER, countable=SINGULAR): CorrectionPreposition('lol'),
                #     Trait(gender=NEUTER, countable=PLURAL): CorrectionSuffix('es'),
                #     Trait(gender=MALE, countable=SINGULAR): CorrectionSuffix(''),
                #     Trait(gender=MALE, countable=PLURAL): CorrectionSuffix('esas'),
                #     Trait(gender=FEMALE, countable=SINGULAR): CorrectionPreposition('la'),
                #     Trait(gender=FEMALE, countable=PLURAL): CorrectionSuffix('esania'),
                # }

    def translate_word_token(self, token: Token) -> str:
        word_eng_base = token.word_base
        word_eng_countable = token.countable

        if word_eng_base in self.dictionary:
            word = self.dictionary[word_eng_base]
        else:  # generate and save
            new_gender = random.choice(GENDERS)
            new_word_base = generate_new_word(word_eng_base)
            word = Word(word_base=new_word_base, gender=new_gender)
            self.dictionary[word_eng_base] = word

        correction = self.grammar[Trait(gender=word.gender, countable=word_eng_countable)]  # countable is from text
        return correction.apply(word.word_base)

    def translate(self, text_word: str) -> str:
        # countable     from    text
        # word          from    genetaor
        # coreection    from    grammar
        word_eng_countable, word_eng_base = determine_text_word(text_word)

        if word_eng_base in self.dictionary:
            word = self.dictionary[word_eng_base]
        else:  # generate and save
            new_gender = random.choice(GENDERS)
            new_word_base = generate_new_word(word_eng_base)
            word = Word(word_base=new_word_base, gender=new_gender)
            self.dictionary[word_eng_base] = word

        correction = self.grammar[Trait(gender=word.gender, countable=word_eng_countable)]  # countable is from text
        return correction.apply(word.word_base)

    def get_word(self, eng_word_base, countable):
        word = self.dictionary.get(eng_word_base)
        if word is None:
            return None
        correction = self.grammar[Trait(gender=word.gender, countable=countable)]  # countable is from text
        return correction.apply(word.word_base)


def print_dictionary(lang: Language):
    items = []
    for word_base, word in lang.dictionary.items():
        items.append((
            word_base,
            word,
            lang.get_word(word_base, SINGULAR).title(),
            lang.get_word(word_base, PLURAL).title()
        ))

    for word_base, word, base_singular, base_plural in sorted(items, key=lambda t: t[2]):
        print('{:<10} {:<8} plural: {:<10}  means: {}'.format(base_singular, GENDERS_NAMES[word.gender], base_plural,
                                                              word_base.title()))


def print_grammar(lang: Language):
    for g in GENDERS:
        t_single = Trait(gender=g, countable=SINGULAR)
        t_plural = Trait(gender=g, countable=PLURAL)
        print('{:<10} singular: {:<20} plural: {:<20}'.format(
            GENDERS_NAMES[g],
            str(lang.grammar[t_single]),
            str(lang.grammar[t_plural])
        ))
