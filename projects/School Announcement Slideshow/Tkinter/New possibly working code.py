import pygsheets
import json

def create_google_sheet(sheet_name, credentials_path, new_owner_email):
    # Load credentials from JSON file
    with open(credentials_path, 'r') as f:
        credentials_json = f.read()

    credentials = json.loads(credentials_json)

    # Authorize with Google Sheets using credentials
    gc = pygsheets.authorize(service_account_json=credentials)

    # Create a new Google Sheet
    sh = gc.create(sheet_name)

    # Share the Google Sheet with the new owner
    sh.share(new_owner_email, role='owner')

    print(f"Google Sheets document '{sheet_name}' created. URL: {sh.url}")

if __name__ == "__main__":
    sheet_name = "Test Sheet 123"
    credentials_path = "creds.json"
    new_owner_email = "codingStark09@gmail.com"  # Replace with the desired email address

    create_google_sheet(sheet_name, credentials_path, new_owner_email)
