import pygsheets

# set up credentials
creds_file = 'sodium-lodge-376703-8f5ab782026c.json'
gc = pygsheets.authorize(service_file=creds_file)

# open the Google Sheets document by its URL
sheet_url = 'https://docs.google.com/spreadsheets/d/1Bl0qatKOkC2_boYVE3W0VW01COOucE777mlZywRwg7E/edit#gid=0'
sh = gc.open_by_url(sheet_url)

# select a worksheet by its index (starting from 0)
worksheet = sh[0]

for row in range(1, worksheet.rows):
    if worksheet.cell((row, 3)).value == '':
        availableUserSpot = (f'{row}, 3')
        break
