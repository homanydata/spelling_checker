"""
This file is responsible for interaction with text and docx files
- read dataset text file
- read existing file (text or word doc)
- save to a text file
- save to word doc file
- apply suggestions to a file

"""


def read_dataset() -> tuple(str):
    pass


def read_file(file_path: str) -> str:
    pass


def save_to_file(file_path: str, text: str) -> bool:
    pass


# not to be used outside of this module, just helpers to simpify stuff
def save_to_text_file(file_path:str, text: str) -> bool:
    pass


def save_to_docx_file(file_path:str, text: str) -> bool:
    pass

