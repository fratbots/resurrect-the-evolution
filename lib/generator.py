import sys
import random


class Generator:
    def set_seed(self, seed):
        random.seed(seed)

    def gen_root(self):
        min_syllables = 2
        max_syllables = 4
        syllables_count = random.randrange(
                min_syllables,
                max_syllables
                )
        syllables = self.get_syllables()
        word = []
        for i in range(syllables_count):
            word.append(syllables[random.randrange(len(syllables))])
        return ''.join(word)

    def get_syllables(self,
                      vowels='euioa',
                      consonants='rtpsdfghklzvbnm',
                      ):
        result = []
        for v in vowels:
            for c in consonants:
                result.append('%s%s' % (v, c))
                result.append('%s%s' % (c, v))
        return result
