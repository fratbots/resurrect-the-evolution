import random

from .generator import generator
from .lang import Language
from .lang import print_abc
from .lang import print_dictionary
from .lang import print_grammar


def run(name: str, grammar_file: str, dict_file: str, abc_filenames: list, text_filenames: list):
    random.seed(name)

    language = Language(generator)

    alphabet = language.get_alphabet()
    alphabet_words = []
    with open(abc_filenames[0]) as input:
        content = input.readlines()
        for word in content:
            alphabet_words.append(word.strip().lower())

    with open(abc_filenames[1], 'w') as output:
        output.write(print_abc(language, alphabet, alphabet_words))

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
