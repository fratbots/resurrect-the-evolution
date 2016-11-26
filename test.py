#!/usr/bin/env python3

import random

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


text = '''
A Fairy TALE is a type of short story that typically features folkloric fantasy characters, such as dwarves, elves,
fairies, giants, gnomes, goblins, mermaids, trolls, unicorns, or witches, and usually magic or enchantments.
Fairy tales may be distinguished from other folk narratives such as legends (which generally involve belief in the
veracity of the events described) and explicitly moral tales, including beast fables. The term is mainly used for
stories with origins in European tradition and, at least in recent centuries, mostly relates to children's literature.
This is short sentence. And very short again.
'''.strip()

if __name__ == '__main__':
    random.seed('uprt')

    # new language based on seed
    lang = lib.lang.Language()

    # source text
    print(text)
    print()

    # translated text
    translated_text = translate_sentences(text)
    print(translated_text)
    print()

    # grammars
    lib.lang.print_grammar(lang)
    print()

    # dictionary
    # lib.lang.print_dictionary(lang)
    # print()
