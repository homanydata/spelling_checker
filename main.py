from helper import MSGS, allowed_types
from file_handler import read_file
from types import FunctionType


"""
a module for checking/correcting existing files:
- interact with user, (ask for file path and what option he wants)
- output result if needed
- success or failure with proper exception handling
"""


def input_path(extensions: tuple[str] = None) -> str:
    """
    This asks user for a file path

    Args:
        - extensions (tuple[str]): forces user to input a file of one of certain types, default is None, accepts whatever file
    """
    pass


def input_choice(choices: tuple[str]) -> int:
    """
    lets the user one of certain given options
    """
    pass


def choose_option() -> FunctionType:
    """
    creates options (correct file, save warning/suggestions), uses input_choice, returns the correspoding method
    """
    pass
# maybe I will add some choices later, it depends


def overwrite_file(file_path: str, text: str) -> None:
    """
    This method uses LanguageMaster to overwrite a given file (spelling mistakes) correcting spelling mistakes
    """
    pass


def correct_file(file_path: str, text: str) -> None:
    """
    This method uses LanguageMaster to correct a given file (spelling mistakes) and save corrected version to new file
    """
    pass


def save_warnings(file_path: str, text: str) -> None:
    """
    This method saves a warnings/suggestions file for the user about any spelling mistakes in the given file
    """
    pass


if __name__ == '__main__':
    func = choose_option()
    file = input_path(extensions=allowed_types)
    text = read_file(file)
    func(file, text)


# wait a minute, why is that 2 functions? maybe more scalable but I dont know
# in correction case, well call correct method from langmaster, then save its return to the same file using filehandler
# in saving warnings case, well use helpers' create_warning for every mistake, then write all to a new file, adjacent to the file given
# deos not differ much, can be re-changed easily anw, forget about it