# spelling_checker
This project aims to implement edit distance, and utilize it for basic spelling checking functionality, either through checking user input for spelling mistakes real time through a Tkinter interface, or by reading text/docx files and correcting them.

## Components
### 0. Dataset
Dataset includes 67527 words from [here](https://github.com/neuspell/neuspell/blob/master/data/vocab/tatoeba.txt)

Needed a bit of preparation before using it, done in [preparing_dataset.ipynb](preparing_dataset.ipynb)

### 1. Edit Distance
This module provides an implementation of the edit distance algorithm (2 ways, iterative & recursive), in addition to 2 methods to print out the edit distance table, or get the steps needed to change string 1 to string 2.


### 2. Suggestor
LanguageMaster class is the one that does the 'thinking' and takes decisions behind the scenes:
- Saves the dataset as attribute
- Checks if a given word is correct (if in dataset)
- Suggests n most similar words to a given mispelled word
- Create correction for a given long string (many words)

### 3. File Handler
This module is reposible for everything related to files:
- read dataset text file
- read existing file (text or word doc)
- save to a text file
- save to word doc file
- apply suggestions to a file

### 4. Helper
This modules as the name suggests is designed to help other modules:
- MSGS constant values
- ERRORS messages
- Create a string represeting a warning, given a mistake and suggestions


### 5. Main
a module for checking/correcting existing files:
- Interact with user, (ask for file path and what option he wants)
- Output result if needed

### 6. Typer
This module utilizes other modules to:
- Show live typing in Tkinter interface
- Display warnings/suggestions on spelling mistakes


## Usage
- Download [Python](https://www.python.org/downloads/)
- Download [this repository](https://github.com/homanydata/spelling_checker/archive/refs/heads/main.zip)

If you want to check an existing file
- Run main.py
- Choose the option you want, one of :
    - Overwrite file by the corrected version
    - Create corrected copy
    - Write warnings/suggestions in a new file
- Insert the file path

To use real time spelling checker:
- Download pyperclip package:
    ```sh
    pip install pyperclip
    ```
- Run typer.py
- start typing, you will see warnings/suggestions displayed below your text as you write.
- At anytime when you finish writing, you can copy the text you have written till now.
