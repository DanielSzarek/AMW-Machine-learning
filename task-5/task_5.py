import re

import spacy
from collections import Counter
from spacy import displacy
from spacy.matcher import Matcher
from spacy.tokenizer import Tokenizer


class SpacyTutorial:
    def __init__(self):
        self.nlp = spacy.load("pl_core_news_sm")
        self.text = ('To jest pierwsze zdanie,'
                     ' którego autorem jest Daniel Szarek. '
                     'Daniel jest studentem na AMW w Gdyni. '
                     'Właśnie kończy ostatni rok studiów '
                     'na tej uczelni.')
        self.doc = self.nlp(self.text)

    def new_task(self, task_text):
        print("\n===============================================")
        print(task_text)

    def sentence_detection(self):
        """Detekcja zdań"""
        sentences = list(self.doc.sents)

        for sentence in sentences:
            print(sentence)

    def tokenization(self):
        """Tokenizacja - wyszukanie indeksów pierwszych znaków każdego wyrazu"""
        for token in self.doc:
            print(token, token.idx)

    def customize_tokenizer(self):
        """Własna tokenizacja przy pomocy wyrażenia regularnego"""
        prefix_re = spacy.util.compile_prefix_regex(self.nlp.Defaults.prefixes)
        suffix_re = spacy.util.compile_suffix_regex(self.nlp.Defaults.suffixes)
        infix_re = re.compile(r'''[/~]''')
        return Tokenizer(self.nlp.vocab, prefix_search=prefix_re.search,
                         suffix_search=suffix_re.search,
                         infix_finditer=infix_re.finditer,
                         token_match=None
                         )

    def custom_tokenization(self):
        """Przy wykorzystaniu własnego tokenizatora rozdzielamy tokeny, które zawierają ukośnik"""
        text = 'Przykład zdanie z zastosowaniem ukośnika: niebieski/granatowy'
        doc = self.nlp(text)
        self.nlp.tokenizer = self.customize_tokenizer()
        print([token.text for token in doc])

    def stop_words(self):
        """Stop words jest to zbiór najczęstszych słów w danym języku"""
        spacy_stopwords = spacy.lang.pl.stop_words.STOP_WORDS
        for stopword in list(spacy_stopwords)[:10]:
            print(stopword)

    def remove_stop_words(self):
        for token in self.doc:
            if not token.is_stop:
                print(token)

    def lemmatization(self):
        """Lematyzacja - sprowadzenie formy fleksyjnej do postaci słownikowej"""
        for token in self.doc:
            print(token, token.lemma_)

    def words_frequency(self):
        """Częstość wyrazów z tekście"""
        words = [token.text for token in self.doc if not token.is_stop and not token.is_punct]
        word_freq = Counter(words)
        common_words = word_freq.most_common(5)
        print("NAJCZĘSTSZE SŁOWA")
        print(common_words)
        unique_words = [word for (word, freq) in word_freq.items() if freq == 1]
        print("UNIKALNE SŁOWA")
        print(unique_words)

    def part_of_speeching(self):
        """Wyznaczenie części mowy"""
        for token in self.doc:
            print(token, token.tag_, token.pos_, spacy.explain(token.tag_))

    def find_nouns_and_adj(self):
        """Wyszukanie form gramatycznych takich rzeczowniki i przymiotniki przy pomocy atrybutu pos_"""
        nouns = []
        adjectives = []
        others = []
        for token in self.doc:
            if token.pos_ == 'NOUN':
                nouns.append(token)
            elif token.pos_ == 'ADJ':
                adjectives.append(token)
            else:
                others.append(token)

        print(f"RZECZOWNIKI: {nouns}")
        print(f"PRZYMIOTNIKI: {adjectives}")
        print(f"INNE: {others}")

    def visualization(self):
        """Wizualizacja grafu zależności, który można podejrzeć pod adresem 127.0.0.1:5000,
        funkcja serve() uruchamia serwer HTTP"""
        displacy.serve(self.doc)

    @staticmethod
    def _is_token_allowed(token):
        """Wyłącznie słowa, które nie są stop words oraz nie są znakami interpunkcyjnymi"""
        if not token or not token.string.strip() or token.is_stop or token.is_punct:
            return False
        return True

    @staticmethod
    def _preprocess_token(token):
        """Zmiana wyrazu na zlematyzowaną i z małych liter"""
        return token.lemma_.strip().lower()

    def function_with_preprocess(self):
        """Wstępna obróbka danych przy pomocy powyższych funkcji"""
        complete_filtered_tokens = [self._preprocess_token(token) for token in self.doc if
                                    self._is_token_allowed(token)]
        print(complete_filtered_tokens)

    def extract_phone_number(self):
        doc = self.nlp("Numer do Jana Kowalskiego to: 987-654-321")
        matcher = Matcher(self.nlp.vocab)
        pattern = [{'SHAPE': 'ddd'}, {'ORTH': '-'},
                   {'SHAPE': 'ddd'}, {'ORTH': '-'},
                   {'SHAPE': 'ddd'}]
        matcher.add('PHONE_NUMBER', None, pattern)
        matches = matcher(doc)
        for id, start, end in matches:
            span = doc[start:end]
            print(span.text)

    def dependency_parsing(self):
        """Parsowanie zależności gramatycznej struktury zdania"""
        sentence = "Daniel uczy się spacy"
        doc = self.nlp(sentence)
        for token in doc:
            print(token.text, token.tag_, token.head.text, token.dep_)

    def navigating_tree(self):
        """Możliwość wybierania konkretnej części zdania"""
        one_line_text = "Przykładowy tekst, reprezentujący działanie nawigowania po zdaniu."
        doc = self.nlp(one_line_text)
        print("Sąsiad tokenu nr 4")
        print(doc[2].nbor())
        print("Wszystko na prawo od 3 wyrazu")
        print([token.text for token in doc[4].rights])
        print("Poddrzewo tesktu")
        print(list(doc[3].subtree))

    def shallow_parsing(self):
        """Porcjowanie - proces wybieranie najważniejszych części z nieustruktoryzowanego zdania.
        Dzielimy tekst na frazy."""
        text = "Konferencja medyczna odbędzie się w 12 grudnia 2020 w Gdyni, będzie to wielkie wydarzenie."
        doc = self.nlp(text)
        for chunk in doc.noun_chunks:
            print(chunk)

    def named_entity_recognition(self):
        """Znajdowanie i przydzielenie podobno znaczeniowych encji w nieuporządkowanym tekście
         do predefiniowanych  kategorii."""
        for ent in self.doc.ents:
            print(ent.text, ent.start_char, ent.end_char, ent.label_, spacy.explain(ent.label_))


if __name__ == "__main__":
    st = SpacyTutorial()
    st.new_task("Detekcja zdań")
    st.sentence_detection()
    st.new_task("Tokenizacja")
    st.tokenization()
    st.new_task("Własna tokenizacja")
    st.custom_tokenization()
    st.new_task("Stop words")
    st.stop_words()
    st.new_task("Usunięcie 'stop word' z tekstu")
    st.remove_stop_words()
    st.new_task("Lematyzacja")
    st.lemmatization()
    st.new_task("Częstość słów")
    st.words_frequency()
    st.new_task("Części mowy")
    st.part_of_speeching()
    st.new_task("Wyszukanie danych części mowy")
    st.find_nouns_and_adj()
    st.new_task("Wstępna obróbka danych")
    st.function_with_preprocess()
    st.new_task("Wyciąganie numeru telefonu")
    st.extract_phone_number()
    st.new_task("Paroswanie zależności")
    st.dependency_parsing()
    st.new_task("Nawigowanie po tekście")
    st.navigating_tree()
    st.new_task("Parsowanie w celu znalezenia najważniejszych cześci (Shallow)")
    st.shallow_parsing()
    st.new_task("Przydzielanie do kategorii")
    st.named_entity_recognition()
    st.new_task("Wizualizacja")
    st.visualization()
