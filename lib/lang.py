import collections
import random

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
        pass  # create random rule

    def apply(self, base_word: str) -> str:
        pass


class CorrectionSuffix:
    def __init__(self):
        pass  # create random rule

    def apply(self, base_word: str) -> str:
        pass


CORRECTIONS = [CorrectionPreposition, CorrectionSuffix]


def determine_text_word(word: str) -> (int, str):
    word_eng_countable = PLURAL
    word_eng_base = 'wowowowow'
    return word_eng_countable, word_eng_base


def generate_new_word(word_eng_base: str):
    return 'new_word_base'


class Language:
    def __init__(self):
        self.dictionary = {}  # word_base_eng => Word(word_base, gender)
        self.grammar = {}
        for g in GENDERS:
            for c in COUNTABLE:
                self.grammar[Trait(gender=g, countable=c)] = random.choice(CORRECTIONS)()

    def translate(self, text_word: str) -> str:
        word_eng_countable = PLURAL  # TODO determine by
        word_eng_base = 'asdf'  # for a key

        if word_eng_base in self.dictionary:
            word = self.dictionary[word_eng_base]

        else:  # generate and save
            gender = random.choice(GENDERS)
            word_base = 'asdfasdf'  # todo: generator.generate(word_eng_base)
            word = Word(word_base=word_base, gender=gender)
            self.dictionary[word_eng_base] = word

        correction = self.grammar[Trait(gender=word.gender, countable=word_eng_countable)]  # countable is from text
        return correction.apply(word.word_base)
