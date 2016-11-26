import random

from lib.generator import generator
from lib.types import *


class CorrectionPreposition:
    def __init__(self):
        syllables = generator.get_syllables()
        self.prep = syllables[random.randrange(len(syllables))]

    def apply(self, base_word: str) -> str:
        return self.prep + ' ' + base_word

    def __str__(self):
        return '"{}" + _ + word'.format(self.prep)


class CorrectionSuffix:
    def __init__(self):
        syllables = generator.get_syllables()
        self.suffix = syllables[random.randrange(len(syllables))]

    def apply(self, base_word: str) -> str:
        return base_word + self.suffix

    def __str__(self):
        return 'word + "{}"'.format(self.suffix)


class CorrectionNone:
    def apply(self, base_word: str) -> str:
        return base_word

    def __str__(self):
        return 'word as is'


CORRECTIONS = [CorrectionPreposition, CorrectionSuffix]


class Language:
    def __init__(self):
        self.dictionary = {}  # word_base_eng => Word(word_base, gender)
        self.grammar = {}  # Trait(gender, countable) => correction
        for p in PARTS:
            for g in GENDERS:
                for c in COUNTABLE:
                    trait = Trait(part=p, gender=g, countable=c)
                    correction = CorrectionNone() if p is None else random.choice(CORRECTIONS)()
                    self.grammar[trait] = correction

        # self.grammar = {
        #     Trait(gender=NEUTER, countable=SINGULAR): CorrectionPreposition('lol'),
        #     Trait(gender=NEUTER, countable=PLURAL): CorrectionSuffix('es'),
        #     Trait(gender=MALE, countable=SINGULAR): CorrectionSuffix(''),
        #     Trait(gender=MALE, countable=PLURAL): CorrectionSuffix('esas'),
        #     Trait(gender=FEMALE, countable=SINGULAR): CorrectionPreposition('la'),
        #     Trait(gender=FEMALE, countable=PLURAL): CorrectionSuffix('esania'),
        # }

    def translate_word_token(self, token: Token) -> str:
        # countable     from    text
        # word          from    genetaor
        # correction    from    grammar

        word_eng_base = token.word_base
        word_eng_countable = token.countable

        if word_eng_base in self.dictionary:
            word = self.dictionary[word_eng_base]
        else:
            new_gender = random.choice(GENDERS)
            new_word_base = generator.gen_root(word_eng_base)
            word = Word(word_base=new_word_base, gender=new_gender)
            self.dictionary[word_eng_base] = word

        correction = self.grammar[Trait(part=token.part, gender=word.gender, countable=word_eng_countable)]
        return correction.apply(word.word_base)

    def get_word(self, eng_word_base, countable):
        word = self.dictionary.get(eng_word_base)
        if word is None:
            return None
        correction = self.grammar[Trait(gender=word.gender, countable=countable)]
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
    for p in PARTS:
        print(PARTS_NAMES[p])
        for g in GENDERS:
            t_single = Trait(part=p, gender=g, countable=SINGULAR)
            t_plural = Trait(part=p, gender=g, countable=PLURAL)
            print('{:<10} singular: {:<20} plural: {:<20}'.format(
                GENDERS_NAMES[g],
                str(lang.grammar[t_single]),
                str(lang.grammar[t_plural])
            ))
        print()
