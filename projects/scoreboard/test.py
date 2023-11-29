import tkinter as tk
from PIL import Image, ImageTk, ImageFilter

root = tk.Tk()
root.geometry('500x500')

canvas = tk.Canvas(width=500, height=500)
canvas.pack()

def resize_image(image_path, width, height):
    original_image = Image.open(image_path)
    resized_image = original_image.resize((width, height), resample=Image.LANCZOS)
    return ImageTk.PhotoImage(resized_image)

homeIcon = r"\\vm-file\Student\jstark09\Desktop\codingClass\projects\scoreboard\NCASymbol copy.png"
homeIconPath = homeIcon

imagePosLeft = [75, 100, 100]
img1 = resize_image(homeIconPath, imagePosLeft[2], imagePosLeft[2])
homeIconImage = canvas.create_image(imagePosLeft[0], imagePosLeft[1], anchor=tk.CENTER, image=img1)

root.mainloop()