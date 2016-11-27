import random

from .generator import generator
from .lang import Language
from .lang import print_grammar
from .lang import print_dictionary
from .abc import abc


def run(name: str, grammar_file: str, dict_file: str, abc_filenames: list, text_filenames: list):
    random.seed(name)

    language = Language(generator)

    # abc_dict = abc(abc_filenames[0], abc_filenames[1], language)
    # with open(abc_filenames[0]) as input:
    #     with open(abc_filenames[1], 'w') as output:
    #         language.translate_word_token()

    for input_filename, output_filename in text_filenames:
        with open(input_filename) as input:
            with open(output_filename, 'w') as output:
                text = input.read()
                translated = language.translate(text)
                output.write(translated)

    with open(grammar_file, 'w') as output:
        output.write(print_grammar(language))

    with open(dict_file, 'w') as output:
        output.write(print_dictionary(language))
