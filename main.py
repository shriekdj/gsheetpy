from pprint import pprint
from gsheetpy import GoogleSheetConnector

spreadsheeet = GoogleSheetConnector(
	scopes=["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"],
	creds_path="D:\dev\gsheetspy\gsheetpy\creds.json"
)

sheet = spreadsheeet.open_sheet(
	spreadsheet_id='spread_sheet_id',
	sheet_name="Sheet1")

data = sheet.get_all_records()

pprint(data)