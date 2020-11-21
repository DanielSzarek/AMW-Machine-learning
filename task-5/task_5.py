import spacy


class SpacyTutorial:
    def __init__(self):
        self.nlp = spacy.load("pl_core_news_sm")
        self.text = ('Oto pierwsze zdanie.'
                     'Oto początek drugiego zdania,'
                     'a to jego koniec. W końcu '
                     'ostatnie zdanie.')
        self.doc = self.nlp(self.text)

    def sentence_detection(self):
        """Detekcja zdań"""
        sentences = list(self.doc.sents)

        for sentence in sentences:
            print(sentence)

    def tokenization(self):
        """Tokenizacja - wyszukanie indeksów pierwszych znaków każdego wyrazu"""
        for token in self.doc:
            print(token, token.idx)

    def stop_words(self):
        spacy_stopwords = spacy.lang.pl.stop_words.STOP_WORDS
        for stopword in list(spacy_stopwords)[10]:
            print(stopword)


if __name__ == "__main__":
    st = SpacyTutorial()
    st.sentence_detection()
    st.tokenization()
    st.stop_words()
