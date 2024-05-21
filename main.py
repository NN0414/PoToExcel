import polib
import pandas as pd

def export_to_excel(po_file_path, excel_file_path):
    # Read the PO file
    po = polib.pofile(po_file_path)

    # Collect data to create DataFrame
    data = []

    # Iterate through each entry in the PO file and add it to the data list
    for entry in po:
        if entry.msgid_plural:
            # If msgid_plural exists, add each msgstr to the data list separately
            for idx, msgstr in enumerate(entry.msgstr_plural.values()):
                data.append((entry.msgid_plural, 'msgid_plural', idx, msgstr))
        else:
            # If msgid_plural does not exist, add msgid to the data list
            data.append((entry.msgid, 'msgid', 0, entry.msgstr))

    # Convert data to DataFrame
    df = pd.DataFrame(data, columns=['msgid_plural_or_msgid', 'type', 'msgstr_index', 'msgstr'])

    # Write DataFrame to Excel file
    df.to_excel(excel_file_path, index=False)

# Call the function to export the PO file to Excel
export_to_excel('global.po', 'example.xlsx')
