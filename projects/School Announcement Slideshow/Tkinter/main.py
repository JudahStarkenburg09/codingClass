import tkinter as tk
from tkinter import ttk
from tkinter import messagebox, simpledialog
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import json
import os
from createAndShare import create_google_sheet  # Arguments: create_google_sheet(sheet_name="", shared_emails=[""])
import sys
from datetime import datetime
import threading
from googleapiclient.discovery import build
from google.auth.transport.requests import Request
from google_auth_oauthlib.flow import InstalledAppFlow


class SlideshowApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Slideshow Announcement App")

        # Create labels
        self.large_label = tk.Label(root, text="  Welcome to the slideshow announcement app  ", font=("Helvetica", 16))
        self.large_label.pack(pady=10)

        self.small_label = tk.Label(root, text="Please enter the Google Sheet link for your configuration", font=("Helvetica", 12))
        self.small_label.pack()

        # Create entry box
        self.sheet_link_entry = tk.Entry(root, width=50)
        self.sheet_link_entry.pack(pady=10)

        # Create submit button
        self.submit_button = ttk.Button(root, text="Submit", command=self.submit_sheet_link)
        self.submit_button.pack(pady=10)

        # Create create sheet button
        self.create_sheet_button = ttk.Button(root, text="Don't have a configuration sheet? Create one!", command=self.create_sheet)
        self.create_sheet_button.pack(pady=10)

    def connected(self, sheet, creds, credentials, gc, sheet_key):
        messagebox.showinfo("Success", f"Google Sheet linked successfully!\nSheet Title: {sheet.title}")

        try:
            worksheet = sheet.sheet1  # Assuming it's the first worksheet, adjust if needed
            slides_link = worksheet.acell('K2').value

            if slides_link:
                # Get slideshow name from the Google Slides API
                slideshow_name = self.get_slideshow_name(slides_link, credentials)
                messagebox.showinfo("Slideshow Information", f"Name of Slideshow: {slideshow_name}")
            else:
                messagebox.showinfo("Slideshow Information", "Please provide a link to your announcement slides, and set shared to 'Anyone with the link can view'")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to check Google Slides link.\nError: {str(e)}")
            print(str(e))

        # Clear the contents of the root window
        for widget in self.root.winfo_children():
            widget.destroy()

    def get_slideshow_name(self, slides_link, credentials):
        # Fetch the presentation name using Google Slides API
        try:
            # Setup the Slides API
            service = build('slides', 'v1', credentials=credentials)

            # Extract presentation ID from the link
            presentation_id = slides_link.split('/')[-1]

            # Fetch the presentation
            presentation = service.presentations().get(presentationId=presentation_id).execute()

            # Get the presentation title
            slideshow_name = presentation['title']
            return slideshow_name
        except Exception as e:
            messagebox.showerror("Error", f"Failed to fetch Slideshow information.\nError: {str(e)}")
            return "Unknown Slideshow"


    def load_credentials(self):
        # Check if creds.json exists in the current directory
        if os.path.exists("creds.json"):
            with open("creds.json", "r") as creds_file:
                return json.load(creds_file)
        else:
            # Check if bundled with the executable
            if getattr(sys, 'frozen', False) and hasattr(sys, '_MEIPASS'):
                # If running as a bundled executable, look for creds.json in the bundle directory
                bundled_creds_path = os.path.join(sys._MEIPASS, "creds.json")
                if os.path.exists(bundled_creds_path):
                    with open(bundled_creds_path, "r") as bundled_creds_file:
                        return json.load(bundled_creds_file)
            return None

    def submit_sheet_link(self):
        sheet_link = self.sheet_link_entry.get()

        # Validate if the link is not empty
        if not sheet_link:
            messagebox.showerror("Error", "Please enter a valid Google Sheet link.")
            return

        # Extract Google Sheet key from the link
        try:
            sheet_key = sheet_link.split("/d/")[-1].split("/")[0]
        except IndexError:
            messagebox.showerror("Error", "Invalid Google Sheet link format.")
            return

        # Access Google Sheet using gspread
        try:
            creds = self.load_credentials()
            if creds is None:
                print("Creds is None")
                scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
                credentials = ServiceAccountCredentials.from_json_keyfile_name("creds.json", scope)
            else:
                print("creds is not None")
                credentials = ServiceAccountCredentials.from_json_keyfile_dict(creds)

            gc = gspread.authorize(credentials)
            sheet = gc.open_by_key(sheet_key)
            self.connected(sheet, creds, credentials, gc, sheet_key)

        except Exception as e:
            messagebox.showerror("Error", f"Failed to access the Google Sheet.\nError: {str(e)}")

    def create_sheet(self):
        # Prompt the user for a sheet name
        sheet_name = simpledialog.askstring("Create Sheet", "Enter the name for the new Google Sheet:")

        # Check if the user canceled the input
        if sheet_name is None:
            return

        # Prompt the user for shared emails
        shared_emails = simpledialog.askstring("Create Sheet", "Enter comma-separated emails for sharing (optional):")

        # Convert shared_emails to a list
        shared_emails = [] if shared_emails is None else [email.strip() for email in shared_emails.split(',')]

        # Show preliminary messagebox
        messagebox.showinfo("Creating Sheet", "Creating sheet, this could take up to 5 minutes! You will recieve a message when the operation is complete! Please don't close this window or your sheet could result in corruption or data loss. Press OK to start the operation.")

        try:
            # Call the create_google_sheet function
            now = datetime.now()
            sheet_name += f' ({now.strftime("%d/%m/%Y %H:%M:%S")})'
            link = create_google_sheet(sheet_name=sheet_name, shared_emails=shared_emails)
            self.sheet_link_entry.delete(0, tk.END)  # Clear existing text
            self.sheet_link_entry.insert(0, link)   # Insert the new link
            messagebox.showinfo("Success", f"Google Sheet '{sheet_name}' created successfully!\nSheet Link: {link}")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to create the Google Sheet.\nError: {str(e)}")




if __name__ == "__main__":
    root = tk.Tk()
    app = SlideshowApp(root)
    root.mainloop()


