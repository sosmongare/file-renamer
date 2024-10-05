### Repository Description:

**Repository Name:** `file-renamer`

**Description:**
This repository contains a Python script for renaming files in a directory by appending a specified name to the file's existing name. It's particularly useful for batch renaming PDF files, but can be extended for other file types as well. The script leverages Python's `os` module to traverse and rename files in the specified directory.

---

### README.md File:

You can use the following as your `README.md` file:

```markdown
# File Renamer

This repository contains a Python script for renaming files in bulk by appending a custom name to the existing file names. The script is designed to work with PDF files, but can be adapted for other file types.

## Features

- Renames files by appending a specified string to their names.
- Automatically handles file extensions (currently set for `.pdf` files).
- Simple and easy to customize.

## How to Use

1. Clone the repository:

   ```bash
   git clone https://github.com/sosmongare/file-renamer.git
   ```

2. Navigate to the project directory:

   ```bash
   cd file-renamer
   ```

3. Modify the directory path in the script to point to your folder containing the files to rename.

   In `rename_files.py`, update the `directory` variable to the path where your files are located:

   ```python
   directory = '/path_to_your_folder/Sos Documents'
   ```

4. Run the script:

   ```bash
   python rename_files.py
   ```

   The script will rename all PDF files in the directory, appending " - Sospeter Mongare" to their names.

## Example

If you have a file named `Id Card.pdf`, after running the script, it will be renamed to:

```
Id Card -Sospeter Mongare.pdf
```

## Requirements

- Python 3.x
- Works on Linux, macOS, and Windows.

## License

This project is open-source and available under the MIT License.

```
