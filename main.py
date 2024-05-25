import polib
import os
from openpyxl import Workbook

def export_to_excel(po_file_path, excel_file_path):
    # Before conversion, remove existing file
    if os.path.exists(excel_file_path):
        os.remove(excel_file_path)
    
    # Read the PO file
    po = polib.pofile(po_file_path)

    # Create a new Excel workbook
    wb = Workbook()
    ws = wb.active

    # Write headers
    ws.append(['msgid', 'msgid_plural', 'msgstr_index', 'msgstr'])

    # Write data rows
    for entry in po:
        if entry.msgid_plural:
            for idx, msgstr in enumerate(entry.msgstr_plural.values()):
                ws.append([entry.msgid, entry.msgid_plural, idx, msgstr])
        else:
            ws.append([entry.msgid, ' ', 0, entry.msgstr])
    
    # Save the workbook
    wb.save(excel_file_path)

# Call the function to export the PO file to Excel
export_to_excel('global.po', 'example.xlsx')
