import tkinter as tk
from tkinter import ttk
from datetime import date
import pygsheets
from tkinter import simpledialog
import os
from tkinter import messagebox
from datetime import datetime


current_directory = os.getcwd()
folder1 = 'creds_PrivateDoNotSee'
os.chdir(os.path.join(current_directory, folder1))

# set up credentials
creds_file = 'credentials.json'
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
window.title("Personal Chromebook Check In")
window.config(bg='gray')

label1 = tk.Label(window, text='User Of Chromebook:')
label1.config(bg='gray',fg='black')
label1.place(x=20, y=20)

checkOutTo1 = ttk.Entry(window, width=30)
checkOutTo1.place(x=20,y=40)

label2 = tk.Label(window, text='Chromebook Number:')
label2.config(bg='gray',fg='black')
label2.place(x=20, y=80)

chromebookNumber = ttk.Entry(window, width=30)
chromebookNumber.place(x=20,y=100)

label3 = tk.Label(window, text='Period (1-7/Break/Lunch):')
label3.config(bg='gray',fg='black')
label3.place(x=20, y=140)

chromebookTime = ttk.Entry(window, width=30)
chromebookTime.place(x=20,y=160)

label4 = tk.Label(window, text='Date (Month/Day):')
label4.config(bg='gray',fg='black')
label4.place(x=20, y=200)


chromebookDate = ttk.Entry(window, width=30)
chromebookDate.place(x=20,y=220)


label5 = tk.Label(window, text='Extra Notes:')
label5.config(bg='gray',fg='black')
label5.place(x=300, y=10)

chromebookNotesFrame = ttk.Frame(window)
chromebookNotesFrame.place(x=300, y=30)

chromebookNotesScrollbar = ttk.Scrollbar(chromebookNotesFrame)
chromebookNotesScrollbar.pack(side=tk.RIGHT, fill=tk.Y)

chromebookNotes = tk.Text(chromebookNotesFrame, height=3, width=20, yscrollcommand=chromebookNotesScrollbar.set)
chromebookNotes.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

chromebookNotesScrollbar.config(command=chromebookNotes.yview)




today = date.today()
today_date = today.strftime("%m/%d")
chromebookDate.delete(0, tk.END)
chromebookDate.insert(0, today_date)



def submit():
    for row in range(1, worksheet.rows):
        if worksheet.cell((row, 3)).value == '':
            availableUserSpot = (f'C{row}')
            break
    
    
    availableNumberSpot = (f'B{row}')
    availableTimeSpot = (f'A{row}')
    availableDateSpot = (f'D{row}')
    availableNoteSpot = (f'E{row}')
    availableReturnSpot = (f'F{row}')
    userOfCheckOut = checkOutTo1.get()
    timeOfCheckOut = chromebookTime.get()
    numberOfChromebook = chromebookNumber.get()
    dateOfChromebook = chromebookDate.get()
    notesOfChromebook = chromebookNotes.get('1.0', tk.END)


    if not userOfCheckOut or not timeOfCheckOut or not numberOfChromebook or not dateOfChromebook:
        messagebox.showwarning("Missing Fields", "Please fill out all required fields.")
        return
    
    checkOutTo1.delete(0, tk.END)
    chromebookTime.delete(0, tk.END)
    chromebookNumber.delete(0, tk.END)
    chromebookDate.delete(0, tk.END)
    chromebookNotes.delete("1.0", tk.END)

    

    chromebookDate.delete(0, tk.END)
    chromebookDate.insert(0, today_date)
    
    worksheet.update_value(str(availableUserSpot), str(userOfCheckOut))
    worksheet.update_value(str(availableNumberSpot), str(numberOfChromebook))
    worksheet.update_value(str(availableTimeSpot), str(timeOfCheckOut))
    worksheet.update_value(str(availableDateSpot), str(dateOfChromebook))
    worksheet.update_value(str(availableNoteSpot), str(notesOfChromebook))
    worksheet.update_value(str(availableReturnSpot), 'No')

    messagebox.showinfo("Success", f"Success! Chromebook {numberOfChromebook} was checked out by {userOfCheckOut}")
    

def returnChromebook():
    all_data = worksheet.get_all_values()
    chromebooks = {row[1]: index+1 for index, row in enumerate(all_data[1:]) if row[5] == 'No'}
    

    if not chromebooks:
        messagebox.showinfo("Success", "No Chromebooks Are Checked Out")
    else:
        root = tk.Tk()
        root.withdraw()
        selected = simpledialog.askstring("Select Chromebook", "Please enter the number of the Chromebook you are returning.")
        
        if selected is not None:
            if selected in chromebooks:
                i = chromebooks[selected]
                cell = worksheet.cell((i+1, 6))  # get the cell at row i and column 6
                cell.value = "Yes"  # update the cell value
                cell.update()  # save the changes to the cell
                todayReturn = date.today()
                nowTimeReturn = datetime.now()
                today_dateReturn = todayReturn.strftime("%m/%d/%Y")
                todayTimeReturn = nowTimeReturn.strftime("%H:%M:%S %p")
                dateReturn = today_dateReturn
                person = worksheet.get_value((i+1, 3))
                messagebox.showinfo("Success", f"Chromebook {selected} returned on {dateReturn} (Month/Day), Person Who Checked Out This Chromebook Was {person}")
                returnDate = f"""
Date: {dateReturn}
Time: {todayTimeReturn}                
                """
                worksheet.update_value((i+1, 7), returnDate)
            else:
                messagebox.showwarning("Invalid Selection", "Invalid Chromebook selection.")









submitButton = tk.Button(window, text='     Submit      ', command=submit)
submitButton.config(bg='yellow',fg='dark blue')
submitButton.place(x=20,y=400)


def bind_enter(event):
    submitButton.invoke()

window.bind('<Return>', bind_enter)

returnButton = tk.Button(window, text='     Return A Chromebook      ', command=returnChromebook)
returnButton.config(bg='yellow',fg='dark blue')
returnButton.place(x=300,y=400)

window.mainloop()
