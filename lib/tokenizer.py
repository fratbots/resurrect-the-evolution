import collections
import re

Token = collections.namedtuple('Token', ['type', 'value', 'line', 'column'])


def tokenize(code):
    regs = [
        ('WORD', r'\w+'),
        ('DOT', r'\.'),
        ('OTHER', r'\W+'),
        ('NEWLINE', r'\n'),
    ]
    reg = '|'.join('(?P<%s>%s)' % pair for pair in regs)
    line_num = 1
    line_start = 0
    for mo in re.finditer(reg, code, re.MULTILINE):
        kind = mo.lastgroup
        value = mo.group(kind)
        if kind == 'NEWLINE':
            line_start = mo.end()
            line_num += 1
            yield Token(kind, value, line_num, 0)
        else:
            column = mo.start() - line_start
            yield Token(kind, value, line_num, column)


def sentences_as_a_text(sentence):
    result = []
    for token in sentence:
        result.append(token.value)
    return ''.join(result)


def sentences(text: str):
    sentence = []
    for token in tokenize(text):
        sentence.append(token)
        print(token.type)
        if token.type == 'DOT':
            yield sentence
            sentence = []
            continue
    yield sentence
