from nltk.stem import WordNetLemmatizer

SINGULAR = 1
PLURAL = 2


class Lemmatizer:
    def __init__(self):
        self.wnl = WordNetLemmatizer()

    def get_countable_and_base(self, word):
        lemma = self.wnl.lemmatize(word, 'n')
        plural = PLURAL if word is not lemma else SINGULAR
        return plural, lemma
