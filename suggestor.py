from file_handler import read_dataset
from edit_distance import edit_distance


"""
This module is responsible for 'thinking', finding and correcting spelling mistakes, and suggesting corrections:
- initiate: save dataset as attribute
- suggest n most similar words to a given spelling mistakes
- check_spelling checks if a given word is correct, if in dataset
- create_correction for a given long string (many words)
"""


class LanguageMaster:
    DISTANCE_LIMIT = 3

    def __init__(self):
        self.dataset = read_dataset()

    def suggest(self, word: str, n: int=3) -> list[str]:
        # remove words that surely need more distance than allowed
        suggestions = list(filter(lambda w: abs(len(w) - len(word)) < LanguageMaster.DISTANCE_LIMIT, self.dataset))
        suggestions.sort(key=lambda w: edit_distance(word1=word, word2=w), reverse=False)
        return suggestions[:min(n, len(suggestions))]

    def check_spelling(self, word: str) -> bool:
        return word in self.dataset

    def get_mistakes(self, text: str) -> list[str]:
        # remove everything other than letters and spaces
        cleaned_text = ''.join((character for character in text if character.isalpha() or character in '\n '))
        # create lists of words
        words = cleaned_text.replace('\n', ' ').split(' ')
        # get all spelling mistakes
        mistakes = list(filter(lambda w: not self.check_spelling(w), words))
        return mistakes

    def create_correction(self, text: str) -> str:
        corrected_text = text
        mistakes = self.get_mistakes(text)
        # replace every mistake by its most similar suggestion
        for mistake in mistakes:
            corrections = self.suggest(word=mistake, n=1)
            if corrections:
                corrected_text = corrected_text.replace(f' {mistake} ', f' {corrections[0]} ')
        return corrected_text
