import collections
import random
import zlib
from lib.generator import Generator

import lib.lemmatizer as lem

NEUTER = 0
FEMALE = 2
MALE = 1

GENDERS = (NEUTER, FEMALE, MALE)

SINGULAR = 1
PLURAL = 2

COUNTABLE = (SINGULAR, PLURAL)

Trait = collections.namedtuple('Trait', ['gender', 'countable'])

Word = collections.namedtuple('Word', ['word_base', 'gender'])


class CorrectionPreposition:
    def __init__(self):
        self.prep = random.choice(['la', 'lu', 'lo'])

    def apply(self, base_word: str) -> str:
        return self.prep + ' ' + base_word


class CorrectionSuffix:
    def __init__(self):
        self.suffix = random.choice(['-ebana', '-jova', '-ben'])

    def apply(self, base_word: str) -> str:
        return base_word + self.suffix


CORRECTIONS = [CorrectionPreposition, CorrectionSuffix]

lemmatizer = lem.Lemmatizer()


def determine_text_word(text_word: str) -> (int, str):
    lem_countable, word_eng_base = lemmatizer.get_countable_and_base(text_word)
    word_eng_countable = PLURAL if lem_countable == lem.PLURAL else SINGULAR
    return word_eng_countable, word_eng_base


def gen(word: str):
    syllables = [
        'la',
        'ko',
        'pep',
        'qwu',
        'e',
        'plo',
        'kuo',
    ]

    # random.seed('uprt' + word)
    new_word_syllables = random.sample(syllables, (zlib.crc32(word.encode()) % 3) + 1)
    return ''.join(new_word_syllables) if len(word) > 1 else ''.join(new_word_syllables)[0]

generator = Generator()

def generate_new_word(word_eng_base: str):
    return generator.gen_root(word_eng_base)
    # return gen(word_eng_base)


class Language:
    def __init__(self):
        self.dictionary = {}  # word_base_eng => Word(word_base, gender)
        self.grammar = {}  # Trait(gender, countable) => correction
        for g in GENDERS:
            for c in COUNTABLE:
                self.grammar[Trait(gender=g, countable=c)] = random.choice(CORRECTIONS)()

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
