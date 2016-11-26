import hashlib
import random


class Generator:
    def gen_root(self, orig_word):
        min_syllables = 2
        max_syllables = 4
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


generator = Generator()
