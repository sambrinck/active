#!/bin/env python3


import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pprint


#Authorize the API
scope = [
    'https://www.googleapis.com/auth/drive',
    'https://www.googleapis.com/auth/drive.file'
    ]
creds = ServiceAccountCredentials.from_json_keyfile_name('client_key.json',scope)
client = gspread.authorize(creds)

#Fetch the sheet
sheet = client.open('Sacrament Prayers').sheet1

python_sheet = sheet.get_all_records()
pp = pprint.PrettyPrinter()
pp.pprint(python_sheet)
