#!/usr/bin/env python3

import random
from lib.generator import generator

import lib.lang
from lib.tokenizer import *


def translate_token(token: Token) -> str:
    if token.type == 'WORD':
        new_word = lang.translate_word_token(token)
        if token.value.isupper():
            new_word = new_word.upper()
        elif token.value.istitle():
            new_word = new_word.title()
        return new_word
    else:
        return token.value


def translate_sentences(text: str) -> str:
    result = []
    for token_sentence in sentences(text):
        # todo: base word countable
        sentence = []
        for token in token_sentence:
            sentence.append(translate_token(token))
        result.append(''.join(sentence))
    return ''.join(result)


file = open('apocalypse.txt', 'r')
text = file.read().strip()

if __name__ == '__main__':
    random.seed('uprt')

    lang = lib.lang.Language(generator)

    abc = {
        'e': None,
        'u': None,
        'i': None,
        'o': None,
        'a': None,
        'r': None,
        't': None,
        'p': None,
        's': None,
        'd': None,
        'f': None,
        'g': None,
        'h': None,
        'k': None,
        'l': None,
        'z': None,
        'v': None,
        'b': None,
        'n': None,
        'm': None,
    }

    abc_filling = 0

    for word in text.split('\n'):
        if abc_filling == len(abc):
            break

        new_word = translate_sentences(word).strip()

        try:
            letter = new_word.split(' ')[1][0]
        except IndexError:
            letter = new_word.split(' ')[0][0]

        letter = letter.lower()

        if abc[letter]:
            continue

        print("{} - {}".format(new_word, word))
        abc[letter] = (new_word, word)
        abc_filling += 1
