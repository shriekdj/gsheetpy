# gsheetspy project by Shrikant Dhayje (@shriekdj) 

## Project Code

```python
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
```


```bash
python main.py
```


```python
[{'5': 'CHANGED', 'blue': 'fas', 'hello': 'Entry', 'red': 'Fav Color'},
 {'5': 'Changed Value', 'blue': 'fas', 'hello': 1, 'red': 'Blue'},
 {'5': 5, 'blue': 'blue', 'hello': 'changed value', 'red': 'red'},
 {'5': 5, 'blue': 'blue', 'hello': 'changed value', 'red': 'red'},
 {'5': 5, 'blue': 'blue', 'hello': 'changed value', 'red': 'red'},
 {'5': 5, 'blue': 'blue', 'hello': 'changed value', 'red': 'red'},
 {'5': 5, 'blue': 'blue', 'hello': 'changed value', 'red': 'red'},
 {'5': 5, 'blue': 'blue', 'hello': 'changed value', 'red': 'red'},
 {'5': 5, 'blue': 'blue', 'hello': 'changed value', 'red': 'red'},
 {'5': 5, 'blue': 'blue', 'hello': 'changed value', 'red': 'red'},
 {'5': 5, 'blue': 'blue', 'hello': 'changed value', 'red': 'red'},
 {'5': 5, 'blue': 'blue', 'hello': 'hello', 'red': 'red'},
 {'5': 5, 'blue': 'blue', 'hello': 'hello', 'red': 'red'},
 {'5': 5, 'blue': 'blue', 'hello': 'hello', 'red': 'red'},
 {'5': 'Shreyas', 'blue': 'dsafds', 'hello': 2, 'red': 'Yellow'},
 {'5': 'Priyanka', 'blue': 'dsafdas', 'hello': 3, 'red': 'Pink'},
 {'5': 'Rajesh', 'blue': 'af', 'hello': 4, 'red': 'Green'},
 {'5': 'Varun', 'blue': 'asfd', 'hello': 5, 'red': 'Red'}]
 ```

# Instructions on Running the file

Google Cloud Console -> Your Project -> API and Services

Google Drive API -> Manage -> Credential Option Near the Quotas -> Create Credentials -> Help me choose

Select Google API Again -> Application Data -> No, I'm not using them -> Create Service Account

Create Service Account By ( Project -> Editor )
- Create Account With Whatever the Name You Want for me i chose `gsheetsbot`
- You Will get an email id of the service account


Download the JSON File Provided by them

Then only enable the Google Sheets API from Library Option Just That

**The JSON Credential File Should Be downloaded from _Google Drive API_ not google sheets**

While Creating Credentials Json File You Will get an Service Account Email Id

Goto Your Spreadsheet and Click Share Option and Share the File as Editor With Service Account Email Id
