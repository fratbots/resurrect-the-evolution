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
COUNTABLE_NAMES = {
    SINGULAR: 'singular',
    PLURAL: 'plural'
}

NOUN = 1
VERB = 2
ADJECTIVE = 3
PREPOSITION = 4
ARTICLE = 5

PARTS = (NOUN, VERB, ADJECTIVE, PREPOSITION, ARTICLE, None)
PARTS_NAMES = {
    NOUN: 'Noun',
    VERB: 'Verb',
    ADJECTIVE: 'Adjective',
    PREPOSITION: 'Preposition',
    ARTICLE: 'Article',
    None: 'Others'
}

Trait = collections.namedtuple('Trait', ['part', 'gender', 'countable'])

Word = collections.namedtuple('Word', ['part', 'word_base', 'gender'])

Token = collections.namedtuple('Token', ['type', 'value', 'countable', 'part', 'word_base', 'line', 'column'])
