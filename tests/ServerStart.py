import webview
import threading
import time
import tkinter as tk
import json
import pyautogui
import pygsheets
from tkinter import messagebox

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
sheet_url = 'https://docs.google.com/spreadsheets/d/1nSwma4A-zN0TwHVlf4aMAJw2BmgfgZmq8QFZ189Kl94/edit#gid=0'
sh = gc.open_by_url(sheet_url)

worksheet = sh[0]

def addWhitelist(username, name, server):
    global newRoot
    newRoot.destroy()

    message1 = messagebox.showinfo("Adding", "Please Wait! This May take up to 5 seconds!")

    for i in range(3, 51):
        if str(worksheet.cell(f"J{i}").value) == '':
            print(f"Cell J{i} is blank")
            usernameCell = worksheet.cell(f'J{i}')
            nameCell = worksheet.cell(f'K{i}')
            serverCell = worksheet.cell(f'L{i}')
            break
    
    usernameCell.value = str(username)
    nameCell.value = str(name)
    serverCell.value = str(server)

    usernameCell.update()
    nameCell.update()
    serverCell.update()

    message2 = messagebox.showinfo("Added", "Done!")




def simulate_typing():
    global root
    time.sleep(.5)
    print("Logging in")

    message3 = messagebox.showinfo("Logged In!", "Username: NCAServerStarter, Password; 123NCA")



alreadyLoaded = False

def getWhitelistInfo():
    global newRoot, window
    newRoot = tk.Tk()
    newRoot.title("User Whitelist")

    # Create labels and entry boxes
    username_label = tk.Label(newRoot, text="Username")
    username_label.grid(row=0, column=0, sticky="w")
    username_entry = tk.Entry(newRoot)
    username_entry.grid(row=0, column=1)

    name_label = tk.Label(newRoot, text="Real Name")
    name_label.grid(row=1, column=0, sticky="w")
    name_entry = tk.Entry(newRoot)
    name_entry.grid(row=1, column=1)

    server_label = tk.Label(newRoot, text="Server")
    server_label.grid(row=2, column=0, sticky="w")
    server_entry = tk.Entry(newRoot)
    server_entry.grid(row=2, column=1)

    # Create a button to add to the whitelist
    add_button = tk.Button(newRoot, text="Add to Whitelist", command=lambda: addWhitelist(username_entry.get(), name_entry.get(), server_entry.get()))
    add_button.grid(row=3, column=0, columnspan=2)

    newRoot.mainloop()


def getLogin():
    
    global root, alreadyLoaded
    if alreadyLoaded == False:
        alreadyLoaded = True
        root = tk.Tk()
        root.geometry('200x200')
        root.title("Menu")

        # Create a label
        label = tk.Label(root, text="Menu")
        label.pack(pady=10)

        # Create "Yes" button
        yes_button = tk.Button(root, text="Log In", command=simulate_typing)
        yes_button.pack(padx=10, pady=5)

        whitelist = tk.Button(root, text="Request Whitelist", command=getWhitelistInfo)
        whitelist.pack(padx=10, pady=5)

    root.mainloop()

def on_loaded():
    time.sleep(5)
    print("Webview window has fully loaded")
    getLogin()

def main():
    global window
    # Create a webview window
    window_width, window_height = pyautogui.size()
    window = webview.create_window("Aternos Server", "https://aternos.org/server/")
    # Run the webview main loop
    threadTime = threading.Thread(target=on_loaded)
    threadTime.start()
    webview.start()

if __name__ == "__main__":
    main()