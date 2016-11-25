import collections
import random
import re
from pprint import pprint as pp

Token = collections.namedtuple('Token', ['type', 'value', 'line', 'column'])


def gen(word: str) -> str:
    return '1'


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


def translate(text: str) -> str:
    result = []
    words = {}
    for token in tokenize(text):
        if token.type == 'WORD':
            word = token.value
            if word in words:
                new_word = words[word]
            else:
                new_word = gen(word.lower())
            if word.isupper():
                new_word = new_word.upper()
            elif word.istitle():
                new_word = new_word.title()
            result.append(new_word)
        else:
            result.append(token.value)

    return ''.join(result), words


text = '''
A, Fairy TALE is a type of short story that typically features folkloric fantasy characters, such as dwarves, elves,
fairies, giants, gnomes, goblins, mermaids, trolls, unicorns, or witches, and usually magic or enchantments.
Fairy tales may be distinguished from other folk narratives such as legends (which generally involve belief in the
veracity of the events described)[1] and explicitly moral tales, including beast fables. The term is mainly used for
stories with origins in European tradition and, at least in recent centuries, mostly relates to children's literature.
'''

if __name__ == '__main__':
    random.seed('uprt')
    print(text)
    translated_text, words = translate(text)
    print(translated_text)
    pp(words)
