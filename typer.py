import tkinter as tk
import pyperclip
from helper import MSGS, create_warning
from suggestor import LanguageMaster


def copy_text() -> None:
    text = text_entry.get()
    pyperclip.copy(text)


def highlight_mistake(mistake: str) -> None:
    pass


def validate_last_word(curr_text) -> bool:
    if curr_text and curr_text[-1] == ' ':
        word = curr_text.split(' ')[-1]
        if not master.check_spelling(word):
            highlight_mistake(word)
            suggestions = master.suggest(word)
            display_warning(word, suggestions)
    return True


def display_warning(mistake: str, suggestions: list[str]) -> None:
    prev = suggestion_label.cget('text')
    new = prev + '\n' if prev else '' + create_warning(mistake, suggestions)
    suggestion_label.config(text=new)


def handle_exception(error_message: str) -> None:
    pass


# Create the main window
master = LanguageMaster()
root = tk.Tk()
root.geometry('800x600')
root.title(MSGS.TITLE)

# Create and place a label widget
tk.Label(root, text=MSGS.TYPE_IN_LABEL).pack(pady=15, padx=15)

# Create and place a text entry widget
text_entry = tk.Entry(root, validate='key', validatecommand=(root.register(validate_last_word),'%P'))
text_entry.pack(pady=30)

# Create and place a button widget
greet_button = tk.Button(root, text=MSGS.COPY_BUTTON, command=copy_text)
greet_button.pack(pady=15)

# Create and place a label for the suggestion
suggestion_label = tk.Label(root, text='')
suggestion_label.pack(pady=15)

# Start the main event loop
root.mainloop()
