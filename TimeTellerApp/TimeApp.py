from tkinter import *
import tkinter as ttk
import random
import os
from PIL import ImageTk, Image
import time
import json
import pygsheets
import re

creds = json.dumps({
    "type": "service_account",
    "project_id": "linus-co",
    "private_key_id": "5f8ac6ad7e2535d14626e3eeeca3aec93ce19614",
    "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvAIBADANBgkqhkiG9w0BAQEFAASCBKYwggSiAgEAAoIBAQCvBNFv/7FitDdt\nbTpLaDjmuDTQSOHqjwAk98zQCktx3CXh+n0DXXtYMN1+PdsvkwiCPdhtcwaguStV\naQucji5L0C9stgpKPSUcuEJAdwEgHj9mbbb1NgM4s+meKFJFOG69F17LOE3scRiA\nqif79pR4Omtx6gmLai/1Z3hhAD6k9YKmicBY2h/Dl7sk12LHHSifLEHaWmCLxdkl\n9p3KNUjvY8+0BYd7SxTe6bk7Lf8vbCTDBg3jn5/hRgTbmF7coSk9fX5KLE6klFDJ\n3FmHSV5BnNn0Czffr71X5miYeSI2EHStp23azNLKU6JYMnQWwwyaRkR9q5N026ic\nNH1xlsPvAgMBAAECggEADP6slkZD43JCE0vi4ipw3yCaO0TOEV5gwl3rxR6ej2ur\nHGY+1fsg52FpcLAjEBs4rILvCOFbgp99CjBsfklIQrTIcKfrh6uWj9VWhfbQDJRy\nXKaUyQwjnRgupmGUCjOwdTXBAhHCJ2YWTadUpK6gQ3UC+UhJQSK3QN9X3svn2tOI\nWaTLdwR0zQYkwO5UaKm/kx5gYh8/uSI+l100fSC3osX5vFfB16LzGwX9LGVd15Bi\nnqmptj5/OHaSCDkU6mZfHNHyZtpNeA0QIK1CDxIw99r3/+7HPk7mCAUM3kriCbsx\n4NAo0dOhpgL8pUTFeX3APJ/2uvVvdySVOEKhpTH40QKBgQDXoRTuPC21HT298d1K\n+Iw7TR1u1a8+iYNM4ud/2t2bal/bDb4en5a8wHXZut7BGohgVq3VF+zs1d9Y1C4X\nK+bbmRe8FOb9rwbGeGyysJtdXQsuRmWVOzomfV5PPMJXJg9RosbuIVukEgdoFmT8\nh9bIHfYBDTGYWUykD1wrqx6WVQKBgQDPyVDG9/S2VIvFD3X4tv0UoI30xIDyo8Yx\nRHAIPfvH2fLHLYNgDTir+wqJnxxNtd075dvVDVgiGzHuRpf9pI9LQ7/5Fz78cvJv\n0P62SeHf9OGlNmRWTQOeRqQKc5yuaQ+Skz1tarbCrYgrF4juBabWMgSJ/k3fFrdM\nRApouOqNMwKBgGzgLdRY2G9hs2IsNKN9OjlbJ6hmBtVZ081HqMJa/ZhSrtHJb5zA\n0fi+aQMmIwF35zJVsfIt4Xh4SQzuHdOfXDK3a0+RckzXSmF+Psw+9kO/Dj0wWGxw\nel0i4jK6KBqe4g9DVJS6jS4b2FeLLzR/Vki3MBa51bfqJxOTmeOGxKv9AoGAZ1y0\nsxV7hQvPr4p+W+fjQ1SO6TirEIiJuc5akK8MxaDUlWI9nRVWoK6z0jv1H28di4NP\ndM87jVPL5cT2LLWkloMwRx/aNEiV8yua2WEtXHP7n2zMQuXyq9RmG9DhGx2mInre\nLsTL/1HFj/IYKpdjI+Ajw+VeJWCuc+DQ8MEz5GMCgYBDMluUqOcRxpHMnXK4g2Ln\nmuyfeih/KhOBQxRWWNvsF7JQ2g+cY+g6yAYt9cRVFXItfkVONSJn58JfBozimEmI\nYffEPg+BVccOS4bf5TqD+bBcAX5GXpq5avat9CZqNbgOKtj2QmlNb7/dGXBZEo2v\noV5xDw7qLdmxY/K+A9mZCg==\n-----END PRIVATE KEY-----\n",
    "client_email": "linus-co-op@linus-co.iam.gserviceaccount.com",
    "client_id": "110264289236205928194",
    "auth_uri": "https://accounts.google.com/o/oauth2/auth",
    "token_uri": "https://oauth2.googleapis.com/token",
    "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
    "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/linus-co-op%40linus-co.iam.gserviceaccount.com"
    })
# set up credentials
gc = pygsheets.authorize(service_account_json=creds)

# open the Google Sheets document by its URL
sheet_url = 'https://docs.google.com/spreadsheets/d/18CwD7AeYmP2FEAfTmW4KbXxmppWhfWB1KiP5ukmGPig/edit#gid=0'
sh = gc.open_by_url(sheet_url)

worksheet = sh[0]


timeApp = ttk.Tk()
timeApp.geometry('800x200')
timeApp.title('Time Teller App')
timeApp.config(bg='gray')
timeApp.resizable(False, False)

current_directory = os.getcwd()
folder1 = 'data'
os.chdir(os.path.join(current_directory, folder1))
Tries = 0

def questionAlreadyAskedTrue():
    global firstTime, distanceBetweenCellsY, distanceBetweenCellsX, photo2, photo, image, listOf9Numbers, startTime, modifiedList, Tries, questionAsked, event, event2, cellHorizontal
    modifiedList = [worksheet.cell(f'D1').value, worksheet.cell(f'E1').value, worksheet.cell(f'F1').value, worksheet.cell(f'G1').value, worksheet.cell(f'H1').value, worksheet.cell(f'I1').value, worksheet.cell(f'J1').value, worksheet.cell(f'K1').value, worksheet.cell(f'L1').value]
    #                        0                             1                             2                             3                            4                             5                           6                             7                           8               
    Yf, mf, df, Hf = worksheet.cell(f'M1').value, worksheet.cell(f'N1').value, worksheet.cell(f'O1').value, worksheet.cell(f'D1').value

    for vertical in range(3):
        # increase vertical direction to make 3x3 grid
        for horizontal in range(3):
            # increase horizontal direction to make 3x3 grid
            gridPosx, gridPosy = (160, 190) #GRID POSITION
            distanceBetweenCellsX, distanceBetweenCellsY = (250, 250) #DISTANCE BETWEEN GRID CELLS
            
            x = horizontal * distanceBetweenCellsX + gridPosx
            y = vertical * distanceBetweenCellsY + gridPosy
            TCanvas.create_image(x, y, image=photo)
                
        TCanvas.create_rectangle(295, 350, 505, 540, fill='gray', outline='gray')

    for v in range(3):
        for h in range(3):
            Y, m, d, H = random.randrange(1,80), random.randrange(1,11), random.randrange(1,28), random.randrange(1,23)
            xText = v * distanceBetweenCellsX + 150
            yText = h * distanceBetweenCellsY + 290
            if v == 1 and h == 1:
                print("center fixed")
                TCanvas.create_text(xText, yText + 40, text=f"{Yf} Years, {mf} Months, {df} Days, and {Hf} Hours", font=("Arial", 12))
            else:
                TCanvas.create_text(xText, yText, text=f"{Y} Years, {m} Months, {d} Days, and {H} Hours", font=("Arial", 8))

    TCanvas.create_text(150, 200, text=f"{modifiedList[1]}%", font=("Arial", 35))
    TCanvas.create_text(400, 200, text=f"{modifiedList[2]}%", font=("Arial", 35))
    TCanvas.create_text(655, 200, text=f"{modifiedList[3]}%", font=("Arial", 35))
    TCanvas.create_text(150, 450, text=f"{modifiedList[4]}%", font=("Arial", 35))

    TCanvas.create_text(400, 450, text=f"{modifiedList[0]}%", font=("Arial", 45))
    
    TCanvas.create_text(655, 450, text=f"{modifiedList[5]}%", font=("Arial", 35))
    TCanvas.create_text(150, 700, text=f"{modifiedList[6]}%", font=("Arial", 35))
    TCanvas.create_text(400, 700, text=f"{modifiedList[7]}%", font=("Arial", 35))
    TCanvas.create_text(655, 700, text=f"{modifiedList[8]}%", font=("Arial", 35))
    TCanvas.create_text(400, 40, text=f"{event}", font=("Arial", 20))


    TCanvas.create_image(415, 440, image=photo2)

questionAsked = False

def tellTheTime():
    global firstTime, distanceBetweenCellsY, distanceBetweenCellsX, photo2, photo, image, listOf9Numbers, startTime, modifiedList, Tries, questionAsked, event, event2, cellHorizontal
    global event
    timeApp.geometry('800x900')
    event2 = str((re.sub(r'[^\w\d]', '', event)).lower())
    event = str(event)
    for prevQ in range(1,3):
        if (str(re.sub(r'[^\w\d]', '', (worksheet.cell(f'A{str(prevQ)}').value)))).lower() == event2:
            questionAsked = True
            cellHorizontal = prevQ
            prevQ = 5
            questionAlreadyAskedTrue()








    print(str(re.sub(r'[^\w\d]', '', (worksheet.cell(f'A1').value))).lower())
    listOf9Numbers = []
    Tries = 0

    if questionAsked == False:
        'Continuing with code...' #not a print!
    else:
        exit()

    def printNumbers():
        global firstTime, distanceBetweenCellsY, distanceBetweenCellsX, photo2, photo, image, listOf9Numbers, startTime, modifiedList, Tries, questionAsked, event, event2, cellHorizontal
        Tries += 1
        endTime = time.time()

        # Make a copy of the original list so that we can modify it without changing the original
        modifiedList = listOf9Numbers[:]

        # Keep subtracting 0.5 from each of the other 8 numbers and adding 4 to the first number
        # until the smallest number is no longer negative

        modifiedList.sort(reverse=True)
        
        going = True
        while going == True:
            if modifiedList[8] > .5:
                modifiedList[0] += 4
                modifiedList[1] -= .5
                modifiedList[2] -= .5
                modifiedList[3] -= .5
                modifiedList[4] -= .5
                modifiedList[5] -= .5
                modifiedList[6] -= .5
                modifiedList[7] -= .5
                modifiedList[8] -= .5

            else: 
                going = False

        # Sort the list in reverse order
        modifiedList.sort(reverse=True)

        # Round each number to one decimal place
        for i in range(9):
            modifiedList[i] = round(modifiedList[i], 1)

        # Print the modified list, the sum of the numbers, the number of tries, and the time it took
        print('\n\n\n\n')
        print(f"Success! {modifiedList} Adds Up To {sum(modifiedList)} With {Tries} Tries! Calculation Took {round(endTime-startTime, 1)} Seconds!")
        print('\n\n\n\n')
        return



    startTime = time.time()
    while True:
        # Generate 9 random numbers using a normal distribution with mean 17.5 and std dev 5
        randomList = [round(random.gauss(17.5, 5), 1) for _ in range(9)]
        # Clip the random numbers to be between 1 and 30
        randomList = [max(min(num, 30), 1) for num in randomList]
        # Adjust the random numbers to sum to 100
        factor = 100 / sum(randomList)
        randomList = [round(num * factor, 1) for num in randomList]
        # Check if the adjustment resulted in any negative numbers
        if all(num >= 0 for num in randomList):
            listOf9Numbers = randomList
            printNumbers()
            break
        else:
            currentTime = time.time()
            Tries += 1
            print(f"Combination Failed! {randomList} Adds Up To {sum(randomList)}")







    def findAllOutcomes(photo):
        global firstTime, distanceBetweenCellsY, distanceBetweenCellsX, photo2, image, listOf9Numbers, startTime, modifiedList, Tries
        # make a grid?
        for vertical in range(3):
            # increase vertical direction to make 3x3 grid
            for horizontal in range(3):
                # increase horizontal direction to make 3x3 grid
                gridPosx, gridPosy = (160, 190) #GRID POSITION
                distanceBetweenCellsX, distanceBetweenCellsY = (250, 250) #DISTANCE BETWEEN GRID CELLS
                
                x = horizontal * distanceBetweenCellsX + gridPosx
                y = vertical * distanceBetweenCellsY + gridPosy
                TCanvas.create_image(x, y, image=photo)
                
        TCanvas.create_rectangle(295, 350, 505, 540, fill='gray', outline='gray')



    def insertText():
        global firstTime, distanceBetweenCellsY, distanceBetweenCellsX, photo2, photo, image, listOf9Numbers, startTime, modifiedList, Tries
        for v in range(3):
            for h in range(3):
                Y, m, d, H = random.randrange(1,80), random.randrange(1,11), random.randrange(1,28), random.randrange(1,23)
                xText = v * distanceBetweenCellsX + 150
                yText = h * distanceBetweenCellsY + 290
                if v == 1 and h == 1:
                    print("center fixed")
                    TCanvas.create_text(xText, yText + 40, text=f"{Y} Years, {m} Months, {d} Days, and {H} Hours", font=("Arial", 12))
                else:
                    TCanvas.create_text(xText, yText, text=f"{Y} Years, {m} Months, {d} Days, and {H} Hours", font=("Arial", 8))
        
    
            
        TCanvas.create_text(150, 200, text=f"{modifiedList[1]}%", font=("Arial", 35))
        TCanvas.create_text(400, 200, text=f"{modifiedList[2]}%", font=("Arial", 35))
        TCanvas.create_text(655, 200, text=f"{modifiedList[3]}%", font=("Arial", 35))
        TCanvas.create_text(150, 450, text=f"{modifiedList[4]}%", font=("Arial", 35))

        TCanvas.create_text(400, 450, text=f"{modifiedList[0]}%", font=("Arial", 45))
        
        TCanvas.create_text(655, 450, text=f"{modifiedList[5]}%", font=("Arial", 35))
        TCanvas.create_text(150, 700, text=f"{modifiedList[6]}%", font=("Arial", 35))
        TCanvas.create_text(400, 700, text=f"{modifiedList[7]}%", font=("Arial", 35))
        TCanvas.create_text(655, 700, text=f"{modifiedList[8]}%", font=("Arial", 35))
        TCanvas.create_text(400, 40, text=f"{event}", font=("Arial", 20))





    findAllOutcomes(photo)
    insertText()

    TCanvas.create_image(415, 440, image=photo2)


    timeApp.mainloop()


def calculateTime():

    global event, TCanvas
    event = inputBox.get()  

    TCanvas = Canvas(timeApp, width=5000, height=5000)
    TCanvas.config(bg='gray')
    TCanvas.pack()

    tellTheTime()

inputBox = ttk.Entry(timeApp, width=45)
inputBox.config(font=("Times New Roman", 20))
inputBox.place(x=80, y=10)


# Open and resize the image
image = Image.open('dial.png')
resized_image = image.resize((330, 196))

# Create the PhotoImage object from the resized image
photo = ImageTk.PhotoImage(resized_image)

resized_image2 = image.resize((450,267))
photo2 = ImageTk.PhotoImage(resized_image2)

submit = ttk.Button(timeApp, text='     Calculate     ', command=calculateTime)
submit.config(height=2, bg='light blue')
submit.place(x=370, y= 50)

timeApp.mainloop()