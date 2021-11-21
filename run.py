#!/usr/bin/env python3

import gspread
from gspread.models import Spreadsheet, Worksheet
from oauth2client.service_account import ServiceAccountCredentials
from active import getActiveMembers 

def updatePrayerSheet(doc : Spreadsheet, members : dict[str:str]):
    WORKSHEET_NAME='Prayer Status'
    numMembers = len(members)
    try:
        status = doc.worksheet(WORKSHEET_NAME)
    except: 
        status = doc.add_worksheet(WORKSHEET_NAME, 300,4, index=1)
    status.resize(cols=3)
    status.resize(rows=3)
    status.clear()
    status.update('A1:C1', [["Name", "Last Prayer Said", "Months since last prayer"]])
    status.format('A1:C1', {'textFormat': {'bold': True}})
    status.update('A2:C', list(members.items()))
    status.update('C2:C', [[f'=DATEDIF(B{i},now(),"M")'] for i in range(2,numMembers+2)], raw=False)
    # status.set_basic_filter()
    print("Range" + f"A2:C{numMembers+1}")
    status.sort((3, 'des'), range=f"A2:C{numMembers+1}")

    # cells = status.range(2,3,2+numMembers,3)
    # cell : gspread.Cell
    # for cell  in cells:
    #     cell.value = f'=DATEDIF(B{cell.row},now(),"M")'
    # status.update_cells(cells, value_input_option='raw')

#Authorize the API
scope = [
    'https://www.googleapis.com/auth/drive',
    'https://www.googleapis.com/auth/drive.file'
    ]
creds = ServiceAccountCredentials.from_json_keyfile_name('client_key.json',scope)
client = gspread.authorize(creds)

#Fetch the sheet
# sheet = client.open('Sacrament Prayers').sheet1
doc = client.open('Sacrament Prayers')

values = doc.sheet1.get_values()
prayers  = dict.fromkeys(getActiveMembers(), None)
for row in values[1:]:
    # print(row)
    for member in row[1:]:
        prayers[member] = row[0]

del prayers[""]
# prayers = sorted(prayers.items(), key=lambda item: item[1])
# for k in prayers.items():
    # print(f"{k}")
updatePrayerSheet(doc, prayers)

# current = doc.sheet1
# prayers = {}
# for row in range(1,current.row_count - 1):
#     print(current.row_values(row))

# python_sheet = current.get_all_records()
# pp = pprint.PrettyPrinter()
# pp.pprint(python_sheet)
