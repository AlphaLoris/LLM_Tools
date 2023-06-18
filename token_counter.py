import tkinter as tk
from tkinter import scrolledtext, messagebox
import tiktoken


def num_tokens_from_string(string: str, encoding_name: str) -> int:
    """Returns the number of tokens in a text string."""
    encoding = tiktoken.get_encoding(encoding_name)
    num_tokens = len(encoding.encode(string))
    return num_tokens


def num_tokens_from_messages(messages, model="gpt-3.5-turbo-0301"):
    # Returns the number of tokens used by a list of messages.
    try:
        encoding = tiktoken.encoding_for_model(model)
    except KeyError:
        encoding = tiktoken.get_encoding("cl100k_base")
    if model == "gpt-3.5-turbo-0301":  # note: future models may deviate from this
        num_tokens = 0
        for message in messages:
            num_tokens += 4  # every message follows <im_start>{role/name}\n{content}<im_end>\n
            num_tokens += len(encoding.encode(message))
        num_tokens += 2  # every reply is primed with <im_start>assistant
        print("num_tokens calculated:", num_tokens)
        return num_tokens
    else:
        raise NotImplementedError(f"num_tokens_from_messages() is not presently implemented for model {model}.")


# Function to count the tokens
def count_tokens():
    # Get the user input from the text box
    user_input = text_box.get("1.0", tk.END)

    # Check if the user input is empty
    if user_input.strip() == "":
        messagebox.showwarning("Warning", "Please enter some text.")
    else:
        # Call the existing function to count the tokens
        num_tokens = num_tokens_from_messages([user_input])

        # Display the number of tokens in the result area
        result_area.configure(text=f"Number of tokens: {num_tokens}")

# Create the main window
window = tk.Tk()

# Set the window title
window.title("Token Counter")

# Set the window size
window.geometry("600x600")

# Set the window padding
window.configure(padx=10, pady=10)

# Create the text box for user input
text_box = scrolledtext.ScrolledText(window, width=70, height=30, padx=10, pady=10)

# Set the text box properties
text_box.pack()

# Create the button frame
button_frame = tk.Frame(window)

# Create the Submit button
submit_button = tk.Button(button_frame, text="Submit", command=count_tokens)

# Create the Clear button
clear_button = tk.Button(button_frame, text="Clear the text box", command=lambda: text_box.delete("1.0", tk.END))

# Create the Cancel button
cancel_button = tk.Button(button_frame, text="Cancel", command=window.destroy)

# Add the buttons to the button frame
submit_button.pack(side="left", padx=10, pady=10)
clear_button.pack(side="left", padx=10, pady=10)
cancel_button.pack(side="left", padx=10, pady=10)

# Add the button frame to the main window
button_frame.pack()

# Create the result area
result_area = tk.Label(window, text="Number of tokens: ")

# Set the result area properties
result_area.pack()

# Run the main loop to start the GUI
window.mainloop()
