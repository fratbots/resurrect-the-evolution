import random


class Generator:
    def get_word(self, seed):
        random.seed(seed)
        max_syllables = 4
        syllables_count = random.randrange(max_syllables)
        syllables = self.get_syllables()
        word = []
        for i in range(syllables_count):
            word.append(syllables[random.randrange(len(syllables))])
        return ''.join(word)

    def get_syllables(self):
        # apparatus
        vowels = 'euioa'
        consonants = 'rtpsdfghklzvbnm'
        # generation
        syllables = []
        for c in consonants:
            for v in vowels:
                syllables.append("%s%s" % (c, v))
                syllables.append("%s%s" % (v, c))
                syllables.append("%s%s%s" % (c, v, c))
        return syllables
