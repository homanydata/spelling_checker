from helper import MSGS, ALLOWED_TYPES, create_warning
from file_handler import read_file, save_to_file, get_extension, get_file_name, get_parent_path
from types import FunctionType
from suggestor import LanguageMaster


"""
a module for checking/correcting existing files:
- interact with user, (ask for file path and what option he wants)
- output result if needed
- success or failure with proper exception handling
"""


def input_path(extensions: list[str] = None) -> str:
    """
    This asks user for a file path

    Args:
        - extensions (list[str]): forces user to input a file of one of certain types, default is None, accepts whatever file
    """
    file_path = input(f'Your file type must be one of {", ".join(extensions)}\ninsert the path of your file: ')
    extension = get_extension(file_path)
    if extension not in extensions:
        return input_path(extensions)
    return file_path


def get_int_from_user(msg, mini=None, maxi=None):
    '''
    This function asks the user for an integer, and makes sure it is bounded as needed
    
    Args:
        - msg (str): question to be asked for the user
        - mini (int): the minimum accepted value (included), default None
        - maxi (int): the maximum accepted value (included), default None
    '''
    answer = input(msg)
    if isnumeric(answer) and (not mini or mini <= int(answer)) and (not maxi or maxi >= int(answer)):
        return int(answer)
    msg = f"Please enter an integer{['',f', minimum {mini}'][mini is not None]}{['', f', maximum {maxi}'][maxi is not None]}: "
    return get_int_from_user(msg, mini, maxi)


def get_user_choice(all_choices: dict) -> int:
    choices_keys = all_choices.keys()
    all_choices = all_choices.values()
    n = len(all_choices)
    # create the question to be asked to user
    msg = f'Choose one of the options below (insert the number you want)\n'
    msg += ''.join([f'{i+1}) {c}\n' for i, c in enumerate(all_choices)])

    chosen_index = get_int_from_user(msg=msg, mini=1, maxi=n)
    return choices_keys[chosen_index]


def choose_option() -> FunctionType:
    """
    creates options (correct file, save warning/suggestions), uses input_choice, returns the correspoding method
    """
    options = {
        overwrite_file: 'Overwrite a file by correcting all spelling mistakes inside it',
        correct_file: 'Correct a file but save correction in a new copy',
        save_warnings: 'Read file and save suggestions and warnings in a new file'
    }
    func = get_user_choice(options)
    return func


def overwrite_file(file_path: str, text: str, master: LanguageMaster) -> None:
    """
    This method uses LanguageMaster to overwrite a given file (spelling mistakes) correcting spelling mistakes
    """
    corrected_text = master.create_correction(text)
    save_to_file(file_path, text=corrected_text)


def correct_file(file_path: str, text: str, master: LanguageMaster) -> None:
    """
    This method uses LanguageMaster to correct a given file (spelling mistakes) and save corrected version to new file
    """
    corrected_text = master.create_correction(text)
    file_name = get_file_name(file_path)
    path = get_parent_path(file_path)
    file_extension = get_extension(file_path)
    save_to_file(f'{path}\\{file_name}_copy_corrected.{file_extension}', text=corrected_text)


def save_warnings(file_path: str, text: str, master: LanguageMaster) -> None:
    """
    This method saves a warnings/suggestions file for the user about any spelling mistakes in the given file
    """
    result = ''
    mistakes = master.get_mistakes(text)
    for mistake in mistakes:
        suggestions = master.suggest(word=mistake)
        result += create_warning(mistake, suggestions)
    file_name = get_file_name(file_path)
    path = get_parent_path(file_path)
    save_to_file(f'{path}\\{file_name}_review.txt')


if __name__ == '__main__':
    master = LanguageMaster()
    func = choose_option()
    file = input_path(extensions=ALLOWED_TYPES)
    text = read_file(file)
    func(file, text, master)
