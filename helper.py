ALLOWED_TYPES = ['txt', 'docx', 'doc']
DATASET_PATH = './cleaned_dataset.txt'


def create_warning(mistake: str, suggestions: list[str]) -> str:
    """
    This method creates a string represeting a warning, given a mistake and suggestions
    """
    suggestions = [f'"{s}"' for s in suggestions]
    return f'Mispelled "{mistake}", did you mean {" or ".join(suggestions)}'

class MSGS:
    HELLO_MSG = "Hello my friend, hope you're fine"
    TITLE = "Spelling Checker"
    COPY_BUTTON = 'Copy'
    TYPE_IN_LABEL = 'Type whatever you want'


class ERRORS:
    ERROR_MSG = lambda e: f'Sorry, an error occured {e}'
    ERROR_SAVING_FILE = lambda file_path: ERRORS.ERROR_MSG(f'while trying to save the file at {file_path}')
    ERROR_READING_FILE = lambda file_path: ERRORS.ERROR_MSG(f'while trying to read the file at {file_path}')
