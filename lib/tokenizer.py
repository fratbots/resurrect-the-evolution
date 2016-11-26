import collections
import re

import nltk

Token = collections.namedtuple('Token', ['type', 'value', 'line', 'column'])


class Tokenizer:
    def is_noun(self, word):
        return self.__is_pos(word, 'NN')

    def is_adjective(self, word):
        return self.__is_pos(word, 'JJ')

    def is_verb(self, word):
        return self.__is_pos(word, 'VB')

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

    def __is_pos(self, word, prefix):
        try:
            tag = self.__pos_tag(word)[0][1]
        except IndexError:
            return False

        return tag.startswith(prefix)

    def __pos_tag(self, word):
        return nltk.pos_tag(nltk.word_tokenize(word))
