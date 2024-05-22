# PO to Excel Converter

## Introduction
This program is a tool designed to convert PO (Gettext Portable Object) files to Excel format. PO files typically contain localization string information for a software application, including original text (`msgid`) and translated text (`msgstr`).

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
     from po_to_excel import export_to_excel
     
     export_to_excel('input.po', 'output.xlsx')
     ```
     - `input.po` is the path to the PO file you want to convert.
     - `output.xlsx` is the path to the output Excel file.

3. **Output**:
   - The program will convert the data from the PO file into Excel format and save it to the specified file.

## Input Format
- The program expects input files to be in standard PO (Gettext Portable Object) file format.

## Output Format
- The output will be an Excel file containing the information from the PO file along with corresponding translation data.

## Data Structure
- The Excel file will contain the following columns:
  - `msgid_plural_or_msgid`: Original text (msgid) or plural-form original text (msgid_plural).
  - `type`: Type of phrase, showing as 'msgid_plural' if it's plural-form, otherwise 'msgid'.
  - `msgstr_index`: If it's a plural-form text, this field indicates which translation it is (starting from 0); if it's singular-form, it's 0.
  - `msgstr`: Corresponding translated text.

## Notes
- Ensure that the PO file format adheres to the standard, as the program may not parse it correctly otherwise.
- Remember to install the necessary Python dependencies before running the program.
