import gspread    #pip install gspread(Need to install package to work on Google sheet)
from gspread import SpreadsheetNotFound
from oauth2client.service_account import ServiceAccountCredentials      #For authentication purpose-Need oauth2client package
from Airtable import employee1 , employee2                          #Importing required data from previous output
scope=['https://www.googleapis.com/auth/spreadsheets','https://www.googleapis.com/auth/drive']
credentials=ServiceAccountCredentials.from_json_keyfile_name('airtable-data.json',scope)    #Applying Credential
client = gspread.authorize(credentials)

try:
    python_test = client.open('Airtable_data').sheet1
    Name = python_test.update_cell(1, 1, "Name")
    Notes = python_test.update_cell(1, 2, "Notes")
    Status = python_test.update_cell(1, 3, "Status")
    python_test.update_cell(2, 1, employee1[1])
    python_test.update_cell(2, 2, employee1[0])
    python_test.update_cell(2, 3, employee1[2])

    python_test.update_cell(3, 1, employee2[1])
    python_test.update_cell(3, 2, employee2[0])
    python_test.update_cell(3, 3, employee2[2])
    print("Successfully completed! Please check you Google sheet")
except SpreadsheetNotFound:
    print("Please check the spreadsheet name")
except AttributeError:
    print("Please check whether attributes are according to Worksheet")
except Exception:
    print("Something went Wrong!")



