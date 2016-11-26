import collections
import random
import hashlib
from lib.generator import Generator

import lib.lemmatizer as lem

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

Word = collections.namedtuple('Word', ['word_base', 'gender'])

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


