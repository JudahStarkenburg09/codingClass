import tkinter as tk
from tkinter import ttk
import pygsheets

# set up credentials
creds_file = 'sodium-lodge-376703-8f5ab782026c.json'
gc = pygsheets.authorize(service_file=creds_file)

# open the Google Sheets document by its URL
sheet_url = 'https://docs.google.com/spreadsheets/d/1Bl0qatKOkC2_boYVE3W0VW01COOucE777mlZywRwg7E/edit#gid=0'
sh = gc.open_by_url(sheet_url)

# select a worksheet by its index (starting from 0)
worksheet = sh[0]

window = tk.Tk()

# Get the screen width and height
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

# Calculate the x and y coordinates to center the window
x = (screen_width/2) - (500/2)
y = (screen_height/2) - (500/2)

# Set the window geometry and position
window.geometry("500x500+{}+{}".format(int(x), int(y)))
window.title("Chromebook Check In")
window.config(bg='gray')

label = tk.Label(window, text='Check Out To:')
label.place(x=50, y=20)

checkOutTo = ttk.Entry(window, width=30)
checkOutTo.place(x=50,y=50)



def submit():
    for row in range(1, worksheet.rows):
        if worksheet.cell((row, 3)).value == '':
            availableUserSpot = (f'C{row}')
            break
    userOfCheckOut = checkOutTo.get()
    worksheet.update_value(str(availableUserSpot), str(userOfCheckOut))

submitButton = tk.Button(window, text='Submit', command=submit)
submitButton.place(x=50,y=300)



window.mainloop()
