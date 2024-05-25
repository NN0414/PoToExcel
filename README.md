# PO to Excel Converter

## Introduction
This tool allows you to convert Gettext Portable Object (PO) files to Excel format, facilitating translation and management.

## Usage
1. **Install Dependencies**:
   - Make sure you have installed the required dependencies: `openpyxl`, `polib`. You can install these dependencies using the following command:
     ```
     pip install polib
     pip install openpyxl
     ```

2. **Run the Program**:
   - Call the `export_to_excel` function as follows:
     ```python 
     export_to_excel('input.po', 'output.xlsx')
     ```
     - `input.po` is the path to the PO file you want to convert, you can replace it if you want it.
     - `output.xlsx` is the path to the output Excel file, you can replace it if you want it.

3. **Output**:
   - The program will convert the data from the PO file into Excel format and save it to the specified file.

## Input Format
- The program expects input files to be in standard PO (Gettext Portable Object) file format.

## Output Format
- The Excel file will contain the following columns:
  - `msgid`: The original text to be translated.
  - `msgid_plural`: The plural form of the original text (if applicable).
  - `msgstr_index`: The index of the translation string (used for plural forms).
  - `msgstr`: The translated text.

## Notes

- Before running the program, make sure you have backed up the original PO file to prevent data loss.
- If an Excel file with the same name already exists at the target path, it will be overwritten.
