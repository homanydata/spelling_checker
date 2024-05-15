import tkinter as tk
from helper import MSGS


def highlight_mistake(mistake: str) -> None:
    pass


def display_warning(mistake: str, suggestions: tuple(str)) -> None:
    pass
    # name = name_entry.get()
    # greeting_label.config(text=f"Hello, {name}!")


def handle_exception(error_message: str) -> None:
    pass


# Create the main window
root = tk.Tk()
root.title(MSGS.TITLE)

# Create and place a label widget
tk.Label(root, text=MSGS.TYPE_IN_LABEL).pack(pady=5)

# Create and place a text entry widget
name_entry = tk.Entry(root)
name_entry.pack(pady=5)

# Create and place a button widget
# NOW I DECIDED A COPY BUTTON WOULD BE BENEFICIAL, OR SAVE BUTTON, DECIDE LATER
greet_button = tk.Button(root, text=MSGS.COPY_BUTTON, command=greet)
greet_button.pack(pady=5)

# Create and place a label for the greeting
greeting_label = tk.Label(root, text='')
greeting_label.pack(pady=5)

# Start the main event loop
root.mainloop()
