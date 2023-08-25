import os
import datetime


def rename_files(directory):
    """Renames all the files in the given directory so that they sort by date."""
    files = os.listdir(directory)
    for file in files:
        filename, extension = os.path.splitext(file)

        # Extracting the month and year from the filename
        try:
            parts = filename.split("-")
            month = parts[1]
            year = parts[2]
            date_str = f"{month}-{year}"
            file_date = datetime.datetime.strptime(date_str, "%b-%Y")
            new_filename = f"{file_date.strftime('%Y%m')}-{month}-{year}{extension}"
            os.rename(os.path.join(directory, file), os.path.join(directory, new_filename))
        except (IndexError, ValueError):
            print(f"Failed to process file: {file}. Skipping...")


if __name__ == "__main__":
    directory = "C:\\Users\\glenn\\OneDrive\\Documents\\Glenn's Docs\\Banking Files\\Taxes 2022\\Paypal"
    rename_files(directory)

