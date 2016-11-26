import collections
import random

import lib.lemmatizer as lem
from lib.generator import Generator
from lib.tokenizer import Tokenizer

NEUTER = 0
FEMALE = 2
MALE = 1

GENDERS = (NEUTER, FEMALE, MALE)
GENDERS_NAMES = {
    NEUTER: 'neuter',
    FEMALE: 'female',
    MALE: 'male'
}

SINGULAR = 1
PLURAL = 2

COUNTABLE = (SINGULAR, PLURAL)

Trait = collections.namedtuple('Trait', ['gender', 'countable'])

Word = collections.namedtuple('Word', ['word_base', 'gender', 'is_noun'])

generator = Generator()
tokenizer = Tokenizer()


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

lemmatizer = lem.Lemmatizer()


def determine_text_word(text_word: str) -> (int, str):
    lem_countable, word_eng_base = lemmatizer.get_countable_and_base(text_word)
    word_eng_countable = PLURAL if lem_countable == lem.PLURAL else SINGULAR
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

    def translate(self, text_word: str) -> str:
        # countable     from    text
        # word          from    genetaor
        # coreection    from    grammar
        word_eng_countable, word_eng_base = determine_text_word(text_word)

        if word_eng_base in self.dictionary:
            word = self.dictionary[word_eng_base]
        elif tokenizer.is_noun(word_eng_base):  # generate and save
            new_gender = random.choice(GENDERS)
            new_word_base = generate_new_word(word_eng_base)
            word = Word(word_base=new_word_base, gender=new_gender, is_noun=True)
            self.dictionary[word_eng_base] = word
        else:
            new_word_base = generate_new_word(word_eng_base)
            word = Word(word_base=new_word_base, gender=None, is_noun=False)
            self.dictionary[word_eng_base] = word
            return new_word_base

        if tokenizer.is_noun(word_eng_base):
            correction = self.grammar[Trait(gender=word.gender, countable=word_eng_countable)]  # countable is from text
            return correction.apply(word.word_base)
        else:
            return word.word_base

    def get_word(self, eng_word_base, countable):
        word = self.dictionary.get(eng_word_base)
        if word is None:
            return None
        if not word.is_noun:
            return word.word_base

        correction = self.grammar[Trait(gender=word.gender, countable=countable)]  # countable is from text
        return correction.apply(word.word_base)


def print_dictionary(lang: Language):
    items = []
    for eng_word_base, word in lang.dictionary.items():
        items.append(
            (
                eng_word_base,
                word,
                word.is_noun,
                lang.get_word(eng_word_base, SINGULAR).title(),
                lang.get_word(eng_word_base, PLURAL).title()
            )
        )

    for word_base, word, is_noun, base_singular, base_plural in sorted(items, key=lambda t: t[2]):
        if is_noun:
            print('{:<10} {:<8} pl.: {:<10}  means: {}'.format(base_singular, GENDERS_NAMES[word.gender], base_plural,
                                                               word_base.title()))
        else:
            print('{} means:  {}'.format(base_singular, word_base.title()))


def print_grammar(lang: Language):
    for g in GENDERS:
        t_single = Trait(gender=g, countable=SINGULAR)
        t_plural = Trait(gender=g, countable=PLURAL)
        print('{:<5} -- singular: {:<10} plural: {:<10}'.format(
            GENDERS_NAMES[g],
            str(lang.grammar[t_single]),
            str(lang.grammar[t_plural])
        ))
