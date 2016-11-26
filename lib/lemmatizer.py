import nltk
from nltk.stem import WordNetLemmatizer

from lib.lang import ADJECTIVE
from lib.lang import NOUN
from lib.lang import PLURAL
from lib.lang import SINGULAR
from lib.lang import VERB


class Lemmatizer:
    def __init__(self):
        self.wnl = WordNetLemmatizer()

    def get_countable_and_base(self, word):
        lemma = self.wnl.lemmatize(word, 'n')
        plural = PLURAL if word is not lemma else SINGULAR
        part_tuple = nltk.pos_tag(nltk.word_tokenize(word))
        try:
            part = part_tuple[0][1]
            if part.startswith('NN'):
                part = NOUN
            elif part.startswith('VB'):
                part = VERB
            elif part.startswith('JJ'):
                part = ADJECTIVE
            else:
                part = None
        except IndexError:
            part = None

        return plural, part, lemma


lemmatizer = Lemmatizer()
