import hashlib
import random

from lib.types import *


class Generator:
    vowels = 'euioa'
    consonants = 'rtpsdfghklzvbnm'

    CACHE = []

    def get_alphabet(self) -> str:
        return self.vowels + self.consonants

    def gen_root(self, orig_word, part):
        min_syllables = 2
        max_syllables = 4
        if part in (ARTICLE, PREPOSITION):
            min_syllables = 1
            max_syllables = 3
        rand_orig_state = random.getstate()
        random.seed(hashlib.md5(orig_word.encode('utf-8')).digest())
        syllables_count = random.randrange(
            min_syllables,
            max_syllables
        )
        syllables = self.get_syllables()
        word = []
        for i in range(syllables_count):
            word.append(syllables[random.randrange(len(syllables))])
        random.setstate(rand_orig_state)
        return ''.join(word)

    def get_syllables(self, vowels=None, consonants=None):
        if not self.CACHE:
            vowels = vowels if vowels else self.vowels
            consonants = consonants if consonants else self.consonants
            result = []
            for v in vowels:
                for c in consonants:
                    result.append('%s%s' % (v, c))
                    result.append('%s%s' % (c, v))
            random.shuffle(result)
            self.CACHE = result
        return self.CACHE


generator = Generator()
