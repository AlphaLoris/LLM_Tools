import tkinter as tk
from tkinter import messagebox
import keyring


def delete_api_key():
    # 'openai' and 'api_key' are the service name and username you used when setting the password
    api_key = keyring.get_password("openai", "api_key")

    if api_key is None:
        messagebox.showinfo("Error", "No API Key found")
        return

    conf = messagebox.askyesno("Confirmation", f"Do you want to delete API Key: {api_key}?")
    if conf:
        keyring.delete_password("openai", "api_key")
        messagebox.showinfo("Success", "API Key deleted successfully")
    else:
        messagebox.showinfo("Cancelled", "Operation cancelled")


if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw()  # hide main window
    delete_api_key()
