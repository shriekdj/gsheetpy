from cmath import e
from pprint import pprint
import gspread
from oauth2client.service_account import ServiceAccountCredentials
# import csv

# scopes = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]

# creds = ServiceAccountCredentials.from_json_keyfile_name("creds.json", scopes)

# client = gspread.authorize(creds)

# sheet = client.open('Sheets Tutorial').sheet1 # Open the spreadhseet

# data = sheet.get_all_records()  # Get a list of all records

# # Here Indexes Starts With 1 for the row and column
# # First heading also counted as index 1 of the row

# row = sheet.row_values(3)  # Get a specific row
# col = sheet.col_values(3)  # Get a specific column
# cell = sheet.cell(1,2).value  # Get the value of a specific cell


# insertRow = ["changed value", 5, "red", "blue"]
# sheet.insert_row(insertRow, 4)  # Insert the list as a row at index 4

# sheet.update_cell(2,2, "CHANGED")  # Update one cell

# numRows = sheet.get_all_records()[0]  # Get the number of rows in the sheet

# pprint(numRows)

class GoogleSheetConnector:
	def __init__(
		self,
		scopes = [],
		creds_path = '',
		):
		"""
		Connect With Google Sheets by scopes list and cred file location
		Preferred Scopes Are\n
		scopes = [\n
			"https://spreadsheets.google.com/feeds",\n
			'https://www.googleapis.com/auth/spreadsheets',\n
			"https://www.googleapis.com/auth/drive.file",\n
			"https://www.googleapis.com/auth/drive"\n
			]
		creds file can be like 
		creds = "D:\\myfiles\creds.json"
		"""
		if not scopes:
			self.scopes = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]
		else:
			self.scopes = scopes
		
		if not creds_path:
			self.creds = ServiceAccountCredentials.from_json_keyfile_name("D:\dev\gsheetspy\gsheetpy\creds.json", self.scopes)
		else:
			self.creds = ServiceAccountCredentials.from_json_keyfile_name(creds_path, self.scopes)

		self.client = gspread.authorize(self.creds)

# gspread.Worksheet

	def open_sheet(self, spreadsheet_id, sheet_name):
		"""
		spreadsheet_id : Available in sheet id
		sheet_name: name of sheet you want to open

		Returns Worksheet Object An List of Dictionaries\n
		Where Each Dictionary is an record of row\n
		keys are heading and values are row values
		"""
		sheet = self.client.open_by_key(spreadsheet_id).worksheet(sheet_name)
		return sheet
