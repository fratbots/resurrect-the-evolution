#!/usr/bin/env python3

import collections
import random
import re


import lib.lang

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


def translate(text: str, lang: lib.lang.Language) -> str:
    result = []
    for token in tokenize(text):
        if token.type == 'WORD':
            word = token.value
            new_word = lang.translate(word)
            if word.isupper():
                new_word = new_word.upper()
            elif word.istitle():
                new_word = new_word.title()
            result.append(new_word)
        else:
            result.append(token.value)

    return ''.join(result)


text = '''
A, Fairy TALE is a type of short story that typically features folkloric fantasy characters, such as dwarves, elves,
fairies, giants, gnomes, goblins, mermaids, trolls, unicorns, or witches, and usually magic or enchantments.
Fairy tales may be distinguished from other folk narratives such as legends (which generally involve belief in the
veracity of the events described)[1] and explicitly moral tales, including beast fables. The term is mainly used for
stories with origins in European tradition and, at least in recent centuries, mostly relates to children's literature.
'''


def print_dictionary(lang: lib.lang.Language):
    genders = {
        lib.lang.NEUTER: 'neuter',
        lib.lang.MALE: 'male',
        lib.lang.FEMALE: 'female',
    }

    items = []
    for eng_word_base, word in lang.dictionary.items():
        items.append(
            (
                eng_word_base,
                word,
                lang.get_word(eng_word_base, lib.lang.SINGULAR).title(),
                lang.get_word(eng_word_base, lib.lang.PLURAL).title()
            )
        )

    for eng_word_base, word, base_singular, base_plural in sorted(items, key=lambda t: t[2]):
        print('{} ({}, plural: {})\n  {} (eng)\n'.format(base_singular, genders[word.gender], base_plural,
                                                         eng_word_base.title()))



def print_grammar(lang: lib.lang.Language):
    for g in lib.lang.GENDERS:
        t_single = lib.lang.Trait(gender=g, countable=lib.lang.SINGULAR)
        t_plural = lib.lang.Trait(gender=g, countable=lib.lang.PLURAL)
        print('{} -- singular: {} plural: {}'.format(lib.lang.GENDERS_NAMES[g], lang.grammar[t_single], lang.grammar[t_plural]))

if __name__ == '__main__':
    sd = 'uprt'
    random.seed(sd)

    # new language based on seed
    lang = lib.lang.Language(sd)

    print(text)
    translated_text = translate(text, lang)
    print(translated_text)
    print_dictionary(lang)
    print_grammar(lang)
    # pp(lang.dictionary)
