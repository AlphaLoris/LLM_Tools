import tkinter as tk
from tkinter import filedialog, messagebox
import os


def parse_and_save_conversations():
    # Create a GUI window and hide it
    root = tk.Tk()
    root.withdraw()

    # Prompt user for source file
    source_filepath = filedialog.askopenfilename(title="Select the source file")
    if not source_filepath:
        messagebox.showinfo("Info", "No source file selected. Exiting.")
        return

    # Prompt user for destination directory
    dest_dir = filedialog.askdirectory(title="Select the destination directory")
    if not dest_dir:
        messagebox.showinfo("Info", "No destination directory selected. Exiting.")
        return

    # Read the content of the source file
    with open(source_filepath, 'r') as file:
        content = file.read()

    # Split the content based on "Title:" pattern
    conversations = [conv for conv in content.split("Title:") if conv.strip()]

    # Iterate through each conversation and save to individual files
    for idx, conversation in enumerate(conversations, start=1):
        title_line = conversation.split("\n")[0].strip()
        filename = f"{idx} - {title_line}.txt"
        filepath = os.path.join(dest_dir, filename)

        with open(filepath, 'w') as file:
            file.write("Title:" + conversation)

    messagebox.showinfo("Success", f"{len(conversations)} conversations saved to {dest_dir}.")


# This function will be called when the script is run
parse_and_save_conversations()
