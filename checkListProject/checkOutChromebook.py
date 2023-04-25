import tkinter as tk
from tkinter import ttk
from datetime import date
import pygsheets
from tkinter import simpledialog
import os
from tkinter import messagebox
from datetime import datetime
import json
import time


creds = json.dumps({
    "type": "service_account",
    "project_id": "sodium-lodge-376703",
    "private_key_id": "8f5ab782026cdfd09476ddcdfd850444abbfb96a",
    "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvgIBADANBgkqhkiG9w0BAQEFAASCBKgwggSkAgEAAoIBAQCxu0PrA/Iz8bio\nW1PkobDRygCDQx4m4L84V515W+9XC4tjlV4ZDzy+cVE0kgXRTM+ON+FkI2Ni93Lf\nBeQ6oWN24LFJBLwvH746aQ54bbZhjNN36VxazeQ3GQ2In3SzEchxNUIRRJWPdCaB\n0fxzi12ovUq/TGEt/p4KsFPgfZ9/FI0lxg1hQxIpW4JXy970Vixu4AquRn57Bsg3\n8C6LlYAtgvM4DxAnvWxhUe2Xseb5UYQWzqykyOsGmnihbJ+p45sphTZQq9fLADvK\n7OOCWmx2ImHSA4/rJ06RJNVO5wCh9jK8s43dffBqDVShbWHCR9avj+m9Cui7jLfq\nYqDrFya/AgMBAAECggEAB/ct28NfvWpV2TS1jkBAAVwcF4Ah5X+I34dBAB9fj3pK\nqQokaucx4IahK2bc58tfFpJXZKYMG2fMtVD5aqq8k7MNrwlTEIqGEtcZtlXwdGP4\n+WkQSrVfgWHvYXsICw/KeNr4hY6aNe42Ofb/0gMn9maToYoOq00wMr9CFUoHsEbj\nbjKC/ouzvry0Cwbht2+Re8US+WArYwHqMUVuR3cKSubSC3Xw5uBlOBvTUjJlJgvf\nHrFEwWsrdD5psMVDl/tLYH3Jt+xTfBnLUffUM0Dj6o64oV9YIOpIG+DoiAqzPP82\n5BJD6DNLLTLsrUBkmCH532InwCjfB/iMidODGkUKOQKBgQDs9XWIOc1i9LdJUILn\nmqAbM2u5HFjEFmkNLw2L83Pzj/rq1Rfi8b62pYi7rjn6QFs9IRo1NQ9kyaTFK9Jc\naeMYgdQ0bRx1VWFtgZr46Kqevyu21swPktgM2Vhto5PSy4tI5U92rgAuGx4GnXNy\n9hAuqRlpgDan6gqRNsO/EiMAZwKBgQDAA2z/9BFGIpzHMnlTN8xSuqCWx/MSxEfE\nt3lOMRdutbAS/see4zOaFqvECmou5kw6LYLRvhXbyEixLmg9DGISO7SSCUFuQHhI\nB6Nco1x3dyodIQmIqmhO7JQV6ZEJQAY9snpusLElFOg5YzaKSZ9QNgArbBbcNZjp\nBWzMAYRP6QKBgDrQ1mKAzm0QhuoItOVd6P23bracxZ+uXFbsZfVl8VL0Wvis+efX\nz1mwjtbe8P8fuEXdEI9CY1bGAkL6lJVhpv+vQgfdSWIKVkuDDv9XaPpMQ0J34GDB\nNyVBUYStRITfBuyKFoZDvEG1c2d672wKjYu3Z1pbe7WEDylqKX4kt1FjAoGBAJmQ\no9Y4nrAW8oglh/7UO2dWtySgGXlC3Zsoma29eV4jlQQ8G+6pCxYLV6hcI/wKV6CX\n0W5pthWmouyBjwB0LOMkORAqste4W/pPkYl/ZW5uMZJGX9ebYfztHKpBuKtLNzKU\n0XJBgguEIw3ymSYUJ4QBDDWuJsJLY1XJ7u9hry4xAoGBAKc/MqsRwz7v+YdKD1FD\nwfR1yi0lEHJMXQ07gR300LzZj0hvlVCBf1izHrpsE1MC3JM03qpFvRU2kVq8srxr\nRo/j0kzWnU+fhgqFg8n4C2DSRdQOqjh5LAtsrrshol/5KSopgxH1Lo2l5mY+YiER\ndZhFt2BA2WrF48ccP0rKWjRm\n-----END PRIVATE KEY-----\n",
    "client_email": "computerlabcheckout@sodium-lodge-376703.iam.gserviceaccount.com",
    "client_id": "117271474767672050840",
    "auth_uri": "https://accounts.google.com/o/oauth2/auth",
    "token_uri": "https://oauth2.googleapis.com/token",
    "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
    "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/computerlabcheckout%40sodium-lodge-376703.iam.gserviceaccount.com"
})

# set up credentials
gc = pygsheets.authorize(service_account_json=creds)

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

label1 = tk.Label(window, text='User Of Chromebook*:')
label1.config(bg='gray',fg='black')
label1.place(x=20, y=20)

checkOutTo1 = ttk.Entry(window, width=30)
checkOutTo1.place(x=20,y=40)

label2 = tk.Label(window, text='Chromebook Number*:')
label2.config(bg='gray',fg='black')
label2.place(x=20, y=80)

chromebookNumber = ttk.Entry(window, width=30)
chromebookNumber.place(x=20,y=100)

chromebooksInStock = worksheet.get_value('H2')
# print(str(chromebooksInStock))

def on_select(value):
    global chromebookTime
    value = value
    chromebookTime = value

    
    



options = ["Unset*", "1st period", "2nd period", "3rd period", "4th period", "5th period", "6th period", "7th period", "Lunch", "Break"]
dropdown_var = tk.StringVar(value=options[0])

dropdown = tk.OptionMenu(window, dropdown_var, *options, command=on_select)
dropdown.config(font=("Arial", 10))
dropdown.place(x=20, y=150)



label4 = tk.Label(window, text="Date Is Automatically Set To Time Of Submit")
label4.config(bg='light gray',fg='red')
label4.place(x=20, y=450)

label6 = tk.Label(window, text="Please Fill Out All Required Fields(*)")
label6.config(bg='light gray',fg='red')
label6.place(x=20, y=430)


label5 = tk.Label(window, text='Extra Notes:')
label5.config(bg='gray',fg='black')
label5.place(x=350, y=10)


# Create the text widget
chromebookNotes = tk.Text(window, height=3, width=20)

# Create the suggestions dropdown menu
suggestions = []

for s_ in range(2,10):
    insideNote = worksheet.get_value(f'I{s_}')
    suggestions.append(insideNote)


notesSuggestionMenu = tk.Listbox(window, height=5)
for s in suggestions:
    notesSuggestionMenu.insert(tk.END, s)

def on_key_press(event):
    global suggestions
    
    notesTyped = event.widget.get("1.0", "end-1c")

    if len(notesTyped) < 3:
        return

    notesSuggestionMenu.delete(0, tk.END)
    for s in suggestions:
        if notesTyped in s:
            notesSuggestionMenu.insert(tk.END, s)
    if notesSuggestionMenu.size() > 0:
        notesSuggestionMenu.place(x=chromebookNotes.winfo_x(), y=chromebookNotes.winfo_y() + chromebookNotes.winfo_height())
    else:
        notesSuggestionMenu.place_forget()

def on_focus_out(event):
    # Hide the dropdown menu when the notes section loses focus
    chromebookNotes.after(100, lambda: notesSuggestionMenu.place_forget())

def on_suggestion_select(event):
    global chromebookNotes, notesSuggestionMenu
    selectedText = notesSuggestionMenu.get(notesSuggestionMenu.curselection())
    chromebookNotes.delete("end-1c linestart", "end")
    chromebookNotes.insert("end-1c", selectedText)
    notesSuggestionMenu.place_forget()

notesSuggestionMenu.bind("<<ListboxSelect>>", on_suggestion_select)

chromebookNotes.bind("<FocusOut>", on_focus_out)
chromebookNotes.bind("<KeyRelease>", on_key_press)

chromebookNotes.place(x=300,y=30)



today = date.today()
dateInsert = today.strftime("%m/%d")
dateCheckout = today.strftime("%m/%d/%Y")
timeCheckoutNow = datetime.now()
timeCheckout = timeCheckoutNow.strftime("%H:%M:%S %p")
today_date = f"""
Date: {dateCheckout}
Time: {timeCheckout}                
                """


def submit():
    global chromebookTime, dropdown_var, value, dropdown
    for row in range(2, worksheet.rows):
        if worksheet.cell((row, 3)).value == '':
            availableUserSpot = (f'C{row}')
            break
    
    chromebookTime = dropdown_var.get()
    
    availableNumberSpot = (f'B{row}')
    availableTimeSpot = (f'A{row}')
    availableDateSpot = (f'D{row}')
    availableNoteSpot = (f'E{row}')
    availableReturnSpot = (f'F{row}')
    userOfCheckOut = checkOutTo1.get()
    periodOfCheckOut = chromebookTime
    numberOfChromebook = chromebookNumber.get()
    notesOfChromebook = chromebookNotes.get('1.0', tk.END)

    # print(f"""
    # User: {userOfCheckOut}
    # Period: {periodOfCheckOut}
    # Number: {numberOfChromebook}
    # Notes?: {notesOfChromebook}
    # """)
    
    failedOnce = False
    if not userOfCheckOut or not numberOfChromebook or periodOfCheckOut == "Unset*":
        messagebox.showwarning("Missing Fields", "Please fill out all required fields.")
        failedOnce = True
        return
    

    try:
        numberOfChromebook = int(numberOfChromebook)
    except ValueError:
        messagebox.showwarning("Fail", "Chrombook Number Must Be A Number")
        return

    if int(numberOfChromebook) < 0 or int(numberOfChromebook) > int(chromebooksInStock) and not failedOnce:
        messagebox.showwarning("Fail", f"Chrombook Number Must Be Between 0 and {chromebooksInStock}")
        return
    failedOnce = False

    checkOutTo1.delete(0, tk.END)

    dropdown.destroy()
    
    options = ["Unset*", "1st period", "2nd period", "3rd period", "4th period", "5th period", "6th period", "7th period", "Lunch", "Break"]
    dropdown_var = tk.StringVar(value=options[0])
    dropdown = tk.OptionMenu(window, dropdown_var, *options, command=on_select)
    dropdown.config(font=("Arial", 10))
    dropdown.place(x=20, y=150)



    chromebookNumber.delete(0, tk.END)
    chromebookNotes.delete("1.0", tk.END)

    
    
    worksheet.update_value(str(availableUserSpot), str(userOfCheckOut))
    worksheet.update_value(str(availableNumberSpot), str(numberOfChromebook))
    worksheet.update_value(str(availableTimeSpot), str(periodOfCheckOut))
    worksheet.update_value(str(availableDateSpot), str(today_date))
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
