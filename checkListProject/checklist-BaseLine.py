import pygsheets

# set up credentials
creds_file = 'sodium-lodge-376703-8f5ab782026c.json'
gc = pygsheets.authorize(service_file=creds_file)

# open the Google Sheets document by its URL
sheet_url = 'https://docs.google.com/spreadsheets/d/1Bl0qatKOkC2_boYVE3W0VW01COOucE777mlZywRwg7E/edit#gid=0'
sh = gc.open_by_url(sheet_url)

# select a worksheet by its index (starting from 0)
worksheet = sh[0]

# update a cell value
worksheet.update_value('A2', 'Lunch')
