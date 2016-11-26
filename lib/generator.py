import random
import itertools


class Generator:
    def gen_root(self, seed):
        random.seed(seed)
        min_syllables = 2
        max_syllables = 4
        syllables_count = random.randrange(
                min_syllables - 1,
                max_syllables - 1
                )
        syllables = self.get_syllables()
        word = []
        for i in range(syllables_count):
            word.append(syllables[random.randrange(len(syllables))])
        return ''.join(word)

    def get_syllables(self,
                      vowels='euioa',
                      consonants='rtpsdfghklzvbnm',
                      min_len=2,
                      max_len=3,
                      allow_vowel_start=True,
                      allow_vowel_end=True,
                      allow_consecutive_vowels=True,
                      allow_similar_consecutive_vowels=True
                      ):
        result = itertools.combinations_with_replacement(
                vowels + consonants,
                max_len
                )
        for r in result:
            if not allow_vowel_start and vowels.find(r[0]) > -1:
                continue
            if not allow_vowel_end and vowels.find(r[:-1]) > -1:
                continue
            # filter results with consecutive consonants
            # TODO filter consecutive vowels
            # TODO filter similar consecutive vowels
            yield ''.join(r)
