#!/usr/bin/env python3

from lib.generator import Generator


def main():
    gen = Generator()
    i = 0
    for s in gen.get_syllables(allow_vowel_start=False):
        print(s)
        i = i + 1
        if i == 1000:
            break


if __name__ == '__main__':
    main()
