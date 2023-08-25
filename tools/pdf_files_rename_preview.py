# Title: Names Preview renaming PDF files in a directory

import os
import re
from tkinter import filedialog, Tk
import PyPDF2


def extract_info_from_pdf(file_path):
    with open(file_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)

        # Check if the PDF file is encrypted
        if reader.is_encrypted:
            reader.decrypt('')

        text = reader.pages[0].extract_text()

        # A naive regex to capture titles; might not work for all PDFs
        title_match = re.search(r'^.*\n', text)
        title = title_match.group(0).strip() if title_match else None

        # A naive regex to capture dates in the format of Month Day, Year
        date_match = re.search(r'(\w+ \d{1,2}, \d{4})', text)
        date = date_match.group(0) if date_match else None

    return title, date


def preview_rename_files_in_directory(directory):
    for file in os.listdir(directory):
        if file.endswith(".pdf"):
            file_path = os.path.join(directory, file)
            title, date = extract_info_from_pdf(file_path)

            # Construct new filename based on title and date
            if title and date:
                new_filename = f"{date} - {title}.pdf"
                print(f"Original: {file}")
                print(f"Proposed: {new_filename}")
                print("-----")


if __name__ == "__main__":
    # Create main window and hide it
    root = Tk()
    root.withdraw()

    directory = filedialog.askdirectory(title="Select a Directory")
    if directory:
        preview_rename_files_in_directory(directory)
