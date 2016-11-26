import re

from lib.lemmatizer import lemmatizer
from lib.types import Token


def tokenize(code):
    regs = [
        ('WORD', r'\w+'),
        ('DOT', r'\.'),
        ('OTHER', r'\W+'),
        ('NEWLINE', r'\n'),
    ]
    reg = '|'.join('(?P<%s>%s)' % pair for pair in regs)
    line = 1
    line_start = 0
    for mo in re.finditer(reg, code, re.MULTILINE):
        kind = mo.lastgroup
        value = mo.group(kind)
        countable, part, word_base = lemmatizer.get_countable_and_base(value)
        word_base = word_base.lower()
        if kind == 'NEWLINE':
            line_start = mo.end()
            line += 1
            yield Token(type=kind, value=value, countable=countable, part=part, word_base=word_base,
                        line=line, column=0)
        else:
            column = mo.start() - line_start
            yield Token(type=kind, value=value, countable=countable, part=part, word_base=word_base,
                        line=line, column=column)


def sentences(text: str):
    sentence = []
    for token in tokenize(text):
        sentence.append(token)
        if token.type == 'DOT':
            yield sentence
            sentence = []
            continue
    yield sentence
