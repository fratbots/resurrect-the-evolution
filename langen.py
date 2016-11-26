#!/usr/bin/env python3

import random
from lib.generator import Generator


def main():
    gen = Generator()
    random.seed("someseed")
    print(gen.gen_root("word_one"))
    print(gen.gen_root("word_two"))


if __name__ == '__main__':
    main()
