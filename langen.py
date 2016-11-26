#!/usr/bin/env python3

from lib.generator import Generator


def main():
    gen = Generator()
    gen.set_seed("someseed")
    print(gen.gen_root())


if __name__ == '__main__':
    main()
