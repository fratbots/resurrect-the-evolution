from lib.lang import Language
from lib.types import *


def abc(input_filename, output_filename, lang: Language):

    alphabet = lang.get_alphabet()
    print(alphabet)
    return

    with open(input_filename) as input:
        with open(output_filename) as output:
            for word in input.readline().lower():
                token = Token(type='WORD', value=word, countable=SINGULAR, part=NOUN, word_base=word, line=0, column=0)
                new_word = lang.translate_word_token(token)

