#!/usr/bin/env python3

import random

import lib.lang
from lib.tokenizer import *


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


# def translate_token_sentence(toke_sentence):


text = '''
A Fairy TALE is a type of short story that typically features folkloric fantasy characters, such as dwarves, elves,
fairies, giants, gnomes, goblins, mermaids, trolls, unicorns, or witches, and usually magic or enchantments.
Fairy tales may be distinguished from other folk narratives such as legends (which generally involve belief in the
veracity of the events described) and explicitly moral tales, including beast fables. The term is mainly used for
stories with origins in European tradition and, at least in recent centuries, mostly relates to children's literature.
This is short sentence. And very short again.
'''


if __name__ == '__main__':
    sd = 'uprt'
    random.seed(sd)

    # new language based on seed
    lang = lib.lang.Language(sd)

    print(text)

    for token_sentence in sentences(text):
        print('{}\n\n'.format(sentences_as_a_text(token_sentence)))
    exit()

    # translated_text = translate(text, lang)
    # print(translated_text)
    lib.lang.print_grammar(lang)
    print()
    lib.lang.print_dictionary(lang)
    # pp(lang.dictionary)
