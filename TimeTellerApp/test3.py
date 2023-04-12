from tkinter import *
import tkinter as tk
import random
import os
from PIL import ImageTk, Image
import time


global firstTime, distanceBetweenCellsY, distanceBetweenCellsX, photo2, photo, image, listOf9Numbers, startTime, modifiedList, Tries
tellTime = tk.Tk()
tellTime.geometry('800x900')
tellTime.title("Time Teller App")
tellTime.config(bg='gray')
tellTime.resizable(False, False)

current_directory = os.getcwd()
folder1 = 'data'
os.chdir(os.path.join(current_directory, folder1))

listOf9Numbers = []
Tries = 0



def printNumbers():
    global firstTime, distanceBetweenCellsY, distanceBetweenCellsX, photo2, photo, image, listOf9Numbers, startTime, modifiedList, Tries
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
            Y, m, d, H = random.randrange(1,70), random.randrange(1,11), random.randrange(1,28), random.randrange(1,23)
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


TCanvas = Canvas(tellTime, width=5000, height=5000)
TCanvas.config(bg='gray')
TCanvas.pack()

# Open and resize the image
image = Image.open('dial.png')
resized_image = image.resize((330, 196))

# Create the PhotoImage object from the resized image
photo = ImageTk.PhotoImage(resized_image)

resized_image2 = image.resize((450,267))
photo2 = ImageTk.PhotoImage(resized_image2)

findAllOutcomes(photo)
insertText()

TCanvas.create_image(415, 440, image=photo2)


tellTime.mainloop()