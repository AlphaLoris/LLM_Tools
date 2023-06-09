import os
import tkinter as tk
from tkinter import filedialog
import tiktoken


def num_tokens_from_messages(messages, model="gpt-3.5-turbo-0301"):
    """Returns the number of tokens used by a list of messages."""
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
        raise NotImplementedError(f"""num_tokens_from_messages() is not presently implemented for model {model}.""")


def split_text(text, max_tokens=4000, separator="\n\n---------divider---------\n\n"):
    blocks = []
    current_block = []
    current_tokens = 0

    messages = text.split("\n")
    for message in messages:
        num_tokens = num_tokens_from_messages([message])
        if current_tokens + num_tokens > max_tokens:
            blocks.append("\n".join(current_block))
            current_block = [message]
            current_tokens = num_tokens
        else:
            current_block.append(message)
            current_tokens += num_tokens

    if current_block:
        blocks.append("\n".join(current_block))

    return separator.join(blocks)


def main():
    root = tk.Tk()
    root.withdraw()

    file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
    if not file_path:
        print("No file selected.")
        return

    with open(file_path, "r", encoding="utf-8") as file:
        text = file.read()

    divided_text = split_text(text)

    new_file_path = os.path.splitext(file_path)[0] + "--divided.txt"
    with open(new_file_path, "w", encoding="utf-8") as file:
        file.write(divided_text)

    print(f"Divided text saved to: {new_file_path}")
    print("---------divider---------")


if __name__ == "__main__":
    main()
