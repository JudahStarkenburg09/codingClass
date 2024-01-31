import pygsheets
from google.oauth2 import service_account

def list_google_sheets(credentials_file):
    # Load service account credentials
    gc = pygsheets.authorize(service_account_file=credentials_file)

    # Get a list of all accessible spreadsheets
    spreadsheets = gc.spreadsheet_titles()

    # Print the list of spreadsheet titles
    for index, title in enumerate(spreadsheets, start=1):
        print(f"{index}. Title: {title}")

    # Ask user for input
    option = input("Enter 1 to delete all sheets, 2 to delete a specific sheet: ")

    if option == '1':
        delete_all_sheets(gc)
    elif option == '2':
        sheet_name = input("Enter the name of the sheet you want to delete: ")
        delete_specific_sheet(gc, sheet_name)
    else:
        print("Invalid option. No action taken.")


def delete_all_sheets(gc):
    # Get a list of all accessible spreadsheets
    spreadsheets = gc.spreadsheet_titles()

    # Confirm deletion
    confirmation = input("Are you sure you want to delete all sheets? (yes/no): ").lower()

    if confirmation == 'yes':
        # Delete all sheets
        for title in spreadsheets:
            # Get the spreadsheet object
            sheet_to_delete = gc.open(title)

            # Delete the spreadsheet
            sheet_to_delete.delete()

        print("All sheets deleted successfully.")
    else:
        print("Deletion canceled.")





def delete_specific_sheet(gc, sheet_name):
    matching_sheets = [title for title in gc.spreadsheet_titles() if sheet_name.lower() in title.lower()]

    if not matching_sheets:
        print(f"No sheets found with the name '{sheet_name}'.")
        return

    print("Matching sheets:")
    for i, title in enumerate(matching_sheets, start=1):
        print(f"{i}. {title}")

    choice = input("Enter the number of the sheet you want to delete (or 0 to cancel): ")
    if not choice.isdigit():
        print("Invalid input. Please enter a number.")
        return

    choice = int(choice)
    if choice == 0 or choice > len(matching_sheets):
        print("Operation canceled.")
        return

    sheet_to_delete = matching_sheets[choice - 1]

    try:
        spreadsheet = gc.open(sheet_to_delete)
        spreadsheet.delete()
        print(f"Sheet '{sheet_to_delete}' successfully deleted.")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    list_google_sheets('creds.json')
