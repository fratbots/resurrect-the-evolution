import random

from .generator import generator
from .lang import Language
from .lang import print_grammar
from .lang import print_dictionary


def run(name, grammar_file, abc_file, dict_file, text_filenames):
    random.seed(name)

    language = Language(generator)

    for input_filename, output_filename in text_filenames:
        with open(input_filename) as input:
            with open(output_filename, 'w') as output:
                text = input.read()
                text2 = language.translate(text)
                output.write(text2)

    with open(grammar_file, 'w') as output:
        output.write(print_grammar(language))

    with open(dict_file, 'w') as output:
        output.write(print_dictionary(language))
