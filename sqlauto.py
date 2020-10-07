from eventPot import select_event, delete_event
import xlrd


def vinEvent(event, location, event_type):
    if event_type.upper() == 'SHIPOUT':
        event_type = ['PO', 'TT']
    elif event_type.upper() == 'TENDER':
        event_type = ['TD']

    loc = "D:\juch01\Desktop\shipout.xlsx"
    wb = xlrd.open_workbook(loc)
    sheet = wb.sheet_by_index(0)
    sheet.cell_value(0, 0)
    vins = []
    for i in range(sheet.nrows):
        vins.append(sheet.cell_value(i, 0))
    if 'SELECT' == event.upper():
        print(select_event(vins, location, event_type))
    elif 'DELETE' == event.upper():
        print(delete_event(vins, location, event_type))

vinEvent('select', 'LZCS', 'tender')


