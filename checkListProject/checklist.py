import gspread
from google.oauth2.service_account import ServiceAccountCredentials

# set up credentials
scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('sodium-lodge-376703-8f5ab782026c.json', scope)
client = gspread.authorize(creds)

# open the Google Sheets document by its URL
sheet_url = 'https://docs.google.com/spreadsheets/d/1Bl0qatKOkC2_boYVE3W0VW01COOucE777mlZywRwg7E/edit#gid=0'
sheet = client.open_by_url(sheet_url)

# select a worksheet by its index (starting from 0)
worksheet = sheet.get_worksheet(0)

# update a cell value
worksheet.update_cell(1, 1, 'New Value')
