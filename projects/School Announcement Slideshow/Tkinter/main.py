import pygsheets
import json
from googleapiclient.discovery import build

def create_google_sheet(sheet_name, credentials_file, new_owner_email):
    # Load service account credentials
    gc = pygsheets.authorize(service_account_file=credentials_file)

    # Create a new Google Sheet
    sh = gc.create(sheet_name)

    # Get the Google Drive file ID of the created sheet
    file_id = sh.id

    # Build the Drive API service
    drive_service = build('drive', 'v3', credentials=gc.credentials)

    # Transfer ownership to the specified email
    drive_service.permissions().create(
        fileId=file_id,
        body={'type': 'user', 'role': 'owner', 'emailAddress': new_owner_email},
        transferOwnership=True
    ).execute()

    print(f"Google Sheets document '{sheet_name}' created. URL: {sh.url}")

if __name__ == "__main__":
    create_google_sheet("Test123", 'creds.json', 'codingStark09@gmail.com')
