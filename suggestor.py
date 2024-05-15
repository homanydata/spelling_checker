from file_handler import read_dataset


"""
This module is responsible for 'thinking', finding and correcting spelling mistakes, and suggesting corrections:
- initiate: save dataset as attribute
- suggest n most similar words to a given spelling mistakes
- check_spelling checks if a given word is correct, if in dataset
- create_correction for a given long string (many words)
"""


class LanguageMaster:
    def __init__(self):
        self.dataset = read_dataset()
    
    def suggest(self, word: str) -> tuple(str):
        pass

    def check_spelling(word: str) -> bool:
        pass

    def create_correction(text: str) -> str:
        pass
