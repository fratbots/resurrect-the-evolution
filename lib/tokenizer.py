import collections
import re

Token = collections.namedtuple('Token', ['type', 'value', 'line', 'column'])

import nltk


class Tokenizer:
    def pos_tag(self, word):
        return nltk.pos_tag(nltk.word_tokenize(word))

    def is_noun(self, word):
        try:
            tag = self.pos_tag(word)[0][1]
        except IndexError:
            return False

        return tag.startswith('NN')

    def tokenize(self, code):
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
