from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
from pydrive.auth import ServiceAccountCredentials
import os
import pygame
import time
import tkinter as tk
from tkinter import ttk, messagebox, IntVar
import threading
import winshell  # Added for creating the shortcut


# Function to load and store a file from Google Drive
def load_and_store_file(file_name, destination_folder, progress_bar):
    # Specify the path to your service account JSON key (jsonCreds.json in this case)
    serviceAccountKeyPath = 'jsonCreds.json'

    # Create GoogleAuth instance and authenticate using service account
    gauth = GoogleAuth()
    gauth.credentials = ServiceAccountCredentials.from_json_keyfile_name(serviceAccountKeyPath, ['https://www.googleapis.com/auth/drive'])

    # Create GoogleDrive instance
    drive = GoogleDrive(gauth)

    # Specify the folder ID of the folder containing your files
    folder_id = '1GR8bDEzfHsWGOdfAq6cLrAIBG-3x9ix9'

    try:
        # Query for the file by name
        query = f"'{folder_id}' in parents and trashed=false and title='{file_name}'"
        file_items = drive.ListFile({'q': query}).GetList()
        if file_items:
            # Create the destination folder structure if it doesn't exist
            if not os.path.exists(destination_folder):
                os.makedirs(destination_folder)

            # Download the file and save it locally in the destination folder
            file_items[0].GetContentFile(os.path.join(destination_folder, file_name))
    except Exception as e:
        print(f'An error occurred while loading {file_name}: {str(e)}')

# List of image and exe file names to load
file_names = [
    'CarHighwayLogo.ico',
    'carTop.png',
    'explosion1.png',
    'explosion2.png',
    'explosion3.png',
    'explosion4.png',
    'explosion5.png',
    'explosion6.png',
    'explosion7.png',
    'obstacleCar1.png',
    'obstacleCar2.png',
    'obstacleCar3.png',
    'road.png',
    'sparks.png',
    # 'jsonCreds.json',
    'Car Highway.exe',  # Add your exe file name here
]

# Folder name to store the images in the Local directory
image_destination_folder = os.path.join(os.getenv('LOCALAPPDATA'), 'Car Highway', 'images')

# Folder name to store the exe file in the Local directory
exe_destination_folder = os.path.join(os.getenv('LOCALAPPDATA'), 'Car Highway')

# Initialize Pygame
pygame.init()

# Create a Tkinter window
window = tk.Tk()
window.title("Car Highway Installer")
window.geometry("400x250")



def createShortcut(exePath):
    desktop = winshell.desktop()
    shortcut = winshell.shortcut(os.path.join(desktop, "Car Highway.lnk"))
    shortcut.path = exePath
    shortcut.write()


def fullIsTrue(progress_bar, increment):
    while progress_bar["value"] < 100:
        progress_bar["value"] += (increment)
        time.sleep(0.2)
    messagebox.showinfo("Installation Complete", "Car Highway has been successfully installed.")
    time.sleep(10)
    exit()

# Checkbox variable
accept_terms = IntVar()

# Create and configure the progress bar
progress_bar = ttk.Progressbar(window, orient="horizontal", length=300, mode="determinate")
progress_bar.pack(pady=10)
full = True
# Function to initiate installation
def install_files():
    global progress_bar, file_names, full, exe_destination_folder, image_destination_folder
    # Check if the user accepted the terms and conditions
    if accept_terms.get() == 1:
        # Disable the button during installation
        install_button.config(state="disabled")
        
        # Start the progress bar at 0%
        progress_bar["value"] = 0
        
        # Calculate the total number of files to download
        total_files = len(file_names)
        
        # Calculate the increment for each file download
        increment = 100 / total_files

        for file_name in file_names:
            if not file_name.endswith('.exe'):
                full_file_path = os.path.join(image_destination_folder, file_name)
                if not os.path.exists(full_file_path):
                    full = False
            elif file_name.endswith('exe'):
                full_file_path = os.path.join(exe_destination_folder, file_name)
                if not os.path.exists(full_file_path):
                    full = False

        if full == True:
            # Create a thread for the installation
            install_thread = threading.Thread(target=fullIsTrue, args=(progress_bar, increment))
            install_thread.start()  # Start the installation thread
        else:
            # Create a thread for the installation
            install_thread = threading.Thread(target=forLoop, args=(progress_bar, increment))
            install_thread.start()  # Start the installation thread
        
    else:
        messagebox.showerror("Error", "Please accept the terms and conditions before installing.")

# Label for terms and conditions
label1 = tk.Label(window, text=f"Terms and Conditions:")
label1.pack()

# Scrollable text box for terms and conditions
text = tk.Text(window, wrap="word", height=8, width=40)
text.pack()
scrollbar = tk.Scrollbar(window, command=text.yview, orient="vertical")
scrollbar.pack(side="right", fill="y")

# Make the text widget read-only
text.config(state="disabled")

termsAndConditions = """
Terms and Conditions

Welcome to Car Highway Game!

These terms and conditions outline the rules and regulations for the use of Car Highway Game's App.

By accessing this app, we assume you accept these terms and conditions. Do not continue to use Car Highway Game if you do not agree to take all of the terms and conditions stated on this page.

The following terminology applies to these Terms and Conditions, Privacy Statement, and Disclaimer Notice and all Agreements: "Client", "You" and "Your" refers to you, the person log on this app and compliant to the Company's terms and conditions. "The Company", "Ourselves", "We", "Our" and "Us", refers to our Company. "Party", "Parties", or "Us", refers to both the Client and ourselves. All terms refer to the offer, acceptance, and consideration of payment necessary to undertake the process of our assistance to the Client in the most appropriate manner for the express purpose of meeting the Client's needs in respect of provision of the Company's stated services, in accordance with and subject to, prevailing law of the Netherlands. Any use of the above terminology or other words in the singular, plural, capitalization, and/or he/she or they, are taken as interchangeable and therefore as referring to the same.

- Car Highway Game is a platform designed for the enjoyment of a virtual car driving experience on the highway.

- While we have taken every precaution to ensure the safety and security of our users, we cannot guarantee that Car Highway Game is completely free from errors, bugs, or vulnerabilities.

- By using Car Highway Game, you agree that the app is provided "as is" and that you use it at your own risk. We will not be held responsible for any direct or indirect damages that may arise from the use of the app.

- Car Highway Game may include links to third-party websites or services that are not under our control. We do not endorse or assume responsibility for the content, privacy policies, or practices of any third-party websites or services.

Thank you for using Car Highway Game and enjoy your virtual driving experience!
"""

text.config(state="normal")  # Enable editing temporarily
text.delete(1.0, tk.END)  # Clear any existing text
text.insert(tk.END, termsAndConditions)
text.config(state="disabled")  # Disable editing agains

# Checkbox for accepting terms and conditions
accept_checkbox = tk.Checkbutton(window, text="I accept the terms and conditions", variable=accept_terms)
accept_checkbox.pack()

# Button to initiate installation
install_button = tk.Button(window, text="Install", command=install_files)
install_button.pack()

# Function to simulate installation with a 5-minute delay
def forLoop(progress_bar, increment):
    global image_destination_folder, file_names, exe_destination_folder
    division = 6
    for file_name in file_names:
        if not file_name.endswith('.exe'):
            load_and_store_file(file_name, image_destination_folder, progress_bar)
            progress_bar["value"] += (increment/division)
            time.sleep(0.5)
            progress_bar["value"] += (increment/division)
            time.sleep(0.5)
            progress_bar["value"] += (increment/division)
            window.update()  # Update the window to refresh the progress bar
            time.sleep(0.5)  # Sleep for a short time to simulate installation
    print("downloaded images")
    
    for file_name in file_names:
        if file_name.endswith('.exe'):
            print("Found and downloading exe")
            load_and_store_file(file_name, exe_destination_folder, progress_bar)
            fileName = file_name

    exePath = os.path.join(exe_destination_folder, fileName)
    createShortcut(exePath)
    
    # Stop the progress bar
    time.sleep(0.5)
    
    progress_bar["value"] += ((((1/division)*3)*increment))
    time.sleep(0.75)
    progress_bar["value"] += ((((1/division)*3)*increment))
    time.sleep(0.75)
    progress_bar["value"] += ((((1/division)*3)*increment))
    time.sleep(0.75)
    progress_bar["value"] = 100


    
    # Show the installation complete message
    messagebox.showinfo("Installation Complete", "Car Highway has been successfully installed.")

# Start the Tkinter main loop
window.mainloop()


#Exe done!