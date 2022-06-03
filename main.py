from pprint import pprint
from gsheetpy import GoogleSheetConnector

spreadsheeet = GoogleSheetConnector()

sheet = spreadsheeet.open_sheet(
	spreadsheet_id='spread_sheet_id',
	sheet_name="Sheet1")

data = sheet.get_all_records()

pprint(data)