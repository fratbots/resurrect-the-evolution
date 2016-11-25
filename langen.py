#!/usr/bin/env python3

from lib.generator import Generator


def main():
    gen = Generator()
    print(gen.get_word("someseed4"))


if __name__ == '__main__':
    main()
