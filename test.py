import collections
import random
import re
import zlib

Token = collections.namedtuple('Token', ['type', 'value', 'line', 'column'])


def tokenize(code):
    token_specification = [
        ('WORD', r'\w+'),
        ('OTHER', r'\W+'),
        ('NEWLINE', r'\n'),
    ]
    tok_regex = '|'.join('(?P<%s>%s)' % pair for pair in token_specification)
    line_num = 1
    line_start = 0
    for mo in re.finditer(tok_regex, code):
        kind = mo.lastgroup
        value = mo.group(kind)
        if kind == 'NEWLINE':
            line_start = mo.end()
            line_num += 1
            yield Token(kind, value, line_num, 0)
        else:
            column = mo.start() - line_start
            yield Token(kind, value, line_num, column)


words = {}

syllables = [
    'la',
    'ko',
    'pep',
    'qwu',
    'e',
    'plo',
    'kuo',
]

def gen(word: str):
    random.seed('uprt' + word)

    new_word_syllables = random.sample(syllables, (zlib.crc32(word.encode()) % 3) + 1)
    return ''.join(new_word_syllables)


statements = '''
A, Fairy TALE is a type of short story that typically features folkloric fantasy characters, such as dwarves, elves,
fairies, giants, gnomes, goblins, mermaids, trolls, unicorns, or witches, and usually magic or enchantments.
Fairy tales may be distinguished from other folk narratives such as legends (which generally involve belief in the
veracity of the events described)[1] and explicitly moral tales, including beast fables. The term is mainly used for
stories with origins in European tradition and, at least in recent centuries, mostly relates to children's literature.
'''

print(statements)

for token in tokenize(statements):
    if token.type == 'WORD':
        print(gen(token.value), end='')
    else:
        print(token.value, end='')
