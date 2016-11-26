import collections

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

NOUN = 1
VERB = 2
ADJECTIVE = 3

PARTS = (None, NOUN, VERB, ADJECTIVE)

Trait = collections.namedtuple('Trait', ['part', 'gender', 'countable'])

Word = collections.namedtuple('Word', ['word_base', 'gender'])

Token = collections.namedtuple('Token', ['type', 'value', 'countable', 'part', 'word_base', 'line', 'column'])
