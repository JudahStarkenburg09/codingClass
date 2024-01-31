from googleapiclient.discovery import build
from google.oauth2 import service_account
import pygsheets

def create_google_sheet(sheet_name, shared_emails=None):
    global service
    credentials_file = 'creds.json'
    
    # Ensure shared_emails is initialized as an empty list if not provided
    shared_emails = shared_emails or []

    # Add default email if not present in the list
    if "codingStark09@gmail.com" not in shared_emails:
        shared_emails.append("codingStark09@gmail.com")

    # Load service account credentials
    gc = pygsheets.authorize(service_account_file=credentials_file)

    # Create a new Google Sheet
    sh = gc.create(sheet_name)

    print(f"Sheet made, {sh.url}")

    # Get the Google Drive file ID of the created sheet
    file_id = sh.id

    scope = ['https://www.googleapis.com/auth/drive']

    credentials = service_account.Credentials.from_service_account_file(
        filename=credentials_file,
        scopes=scope,
    )
    # Build the Drive API service
    service = build('sheets', 'v4', credentials=credentials)

    # Get the sheet ID
    sheet_id = sh.sheet1.id


    def colorCell(sheet_id_var, cellIndexes, colorRGB):
        global service
        # Batch update request to set background color
        batch_update_spreadsheet_request_body = {
            "requests": [
                {
                    "repeatCell": {
                        "range": {
                            "sheetId": sheet_id_var,
                            "startRowIndex": cellIndexes[0],
                            "endRowIndex": cellIndexes[1],
                            "startColumnIndex": cellIndexes[2],
                            "endColumnIndex": cellIndexes[3]
                        },
                        "cell": {
                            "userEnteredFormat": {
                                "backgroundColor": {
                                    "red": colorRGB[0] / 255.0,
                                    "green": colorRGB[1] / 255.0,
                                    "blue": colorRGB[2] / 255.0
                                }
                            }
                        },
                        "fields": "userEnteredFormat.backgroundColor"
                    }
                }
            ]
        }

        # Execute batch update
        request = service.spreadsheets().batchUpdate(spreadsheetId=file_id, body=batch_update_spreadsheet_request_body)
        res = request.execute()

    def set_column_width(worksheet_or_sheet_id, column_index, width):
        # Format the request to set column width
        request = {
            "updateDimensionProperties": {
                "range": {
                    "sheetId": worksheet_or_sheet_id if isinstance(worksheet_or_sheet_id, int) else worksheet_or_sheet_id,
                    "dimension": "COLUMNS",
                    "startIndex": column_index,
                    "endIndex": column_index + 1,
                },
                "properties": {
                    "pixelSize": width,
                },
                "fields": "pixelSize",
            }
        }

        # Execute the request
        service.spreadsheets().batchUpdate(spreadsheetId=file_id, body={"requests": [request]}).execute()

    def set_row_height(worksheet_or_sheet_id, row_index, height):
        # Format the request to set row height
        request = {
            "updateDimensionProperties": {
                "range": {
                    "sheetId": worksheet_or_sheet_id if isinstance(worksheet_or_sheet_id, int) else worksheet_or_sheet_id,
                    "dimension": "ROWS",
                    "startIndex": row_index,
                    "endIndex": row_index + 1,
                },
                "properties": {
                    "pixelSize": height,
                },
                "fields": "pixelSize",
            }
        }

        # Execute the request
        service.spreadsheets().batchUpdate(spreadsheetId=file_id, body={"requests": [request]}).execute()

    def insert_text(sheet_id_var, cell_indexes, text, text_color=None, horizontal_align=None, vertical_align=None):
        global service
        # Batch update request to insert text
        batch_update_spreadsheet_request_body = {
            "requests": [
                {
                    "repeatCell": {
                        "range": {
                            "sheetId": sheet_id_var,
                            "startRowIndex": cell_indexes[0],
                            "endRowIndex": cell_indexes[1],
                            "startColumnIndex": cell_indexes[2],
                            "endColumnIndex": cell_indexes[3],
                        },
                        "cell": {
                            "userEnteredValue": {"stringValue": text},
                            "userEnteredFormat": {"textFormat": {"foregroundColor": {"red": 0, "green": 0, "blue": 0}}},
                        },
                        "fields": "userEnteredValue,userEnteredFormat.textFormat.foregroundColor,userEnteredFormat.horizontalAlignment,userEnteredFormat.verticalAlignment"
                    }
                }
            ]
        }

        # Set text color if provided
        if text_color:
            batch_update_spreadsheet_request_body["requests"][0]["repeatCell"]["cell"]["userEnteredFormat"]["textFormat"]["foregroundColor"] = {
                "red": text_color[0] / 255.0,
                "green": text_color[1] / 255.0,
                "blue": text_color[2] / 255.0
            }

        # Set horizontal alignment if provided
        if horizontal_align:
            batch_update_spreadsheet_request_body["requests"][0]["repeatCell"]["cell"]["userEnteredFormat"]["horizontalAlignment"] = horizontal_align

        # Set vertical alignment if provided
        if vertical_align:
            batch_update_spreadsheet_request_body["requests"][0]["repeatCell"]["cell"]["userEnteredFormat"]["verticalAlignment"] = vertical_align

        # Execute batch update
        request = service.spreadsheets().batchUpdate(spreadsheetId=file_id, body=batch_update_spreadsheet_request_body)
        res = request.execute()



    set_column_width(sheet_id, 0, 150)
    set_row_height(sheet_id, 0, 75)
    colorCell(sheet_id, [0, 1, 0, 1], [153, 153, 153])

    set_column_width(sheet_id, 1, 250)
    set_column_width(sheet_id, 11, 25)
    colorCell(sheet_id, [0, 1, 1, 12], [0, 0, 0])

    insert_text(sheet_id, [0, 1, 1, 2], "Custom Slide Name", text_color=[255, 255, 255], horizontal_align="CENTER", vertical_align="MIDDLE")
    insert_text(sheet_id, [0, 1, 2, 3], "Slide Number", text_color=[255, 255, 255], horizontal_align="CENTER", vertical_align="MIDDLE")
    insert_text(sheet_id, [0, 1, 3, 4], "Sunday", text_color=[255, 255, 255], horizontal_align="CENTER", vertical_align="MIDDLE")
    insert_text(sheet_id, [0, 1, 4, 5], "Monday", text_color=[255, 255, 255], horizontal_align="CENTER", vertical_align="MIDDLE")
    insert_text(sheet_id, [0, 1, 5, 6], "Tuesday", text_color=[255, 255, 255], horizontal_align="CENTER", vertical_align="MIDDLE")
    insert_text(sheet_id, [0, 1, 6, 7], "Wednesday", text_color=[255, 255, 255], horizontal_align="CENTER", vertical_align="MIDDLE")
    insert_text(sheet_id, [0, 1, 7, 8], "Thursday", text_color=[255, 255, 255], horizontal_align="CENTER", vertical_align="MIDDLE")
    insert_text(sheet_id, [0, 1, 8, 9], "Friday", text_color=[255, 255, 255], horizontal_align="CENTER", vertical_align="MIDDLE")
    insert_text(sheet_id, [0, 1, 9, 10], "Saturday", text_color=[255, 255, 255], horizontal_align="CENTER", vertical_align="MIDDLE")

    set_column_width(sheet_id, 2, 175)

    colorCell(sheet_id, [1, 100, 0, 1], [0, 0, 0])
    colorCell(sheet_id, [1, 100, 1, 2], [234, 153, 153])
    colorCell(sheet_id, [1, 100, 2, 3], [255, 217, 102])
    colorCell(sheet_id, [1, 100, 3, 10], [234, 153, 153])
    colorCell(sheet_id, [2, 100, 10, 12], [0, 0, 0])
    colorCell(sheet_id, [1, 2, 11, 12], [0, 0, 0])
    colorCell(sheet_id, [1, 2, 10, 11], [153, 153, 153])
    set_column_width(sheet_id, 10, 400)


    






    # Build the Drive API service
    service = build('drive', 'v3', credentials=credentials)

    if shared_emails:
        for i in shared_emails:
            # Transfer ownership to the specified email
            service.permissions().create(
                fileId=file_id,
                body={
                    'type': 'user',
                    'role': 'writer',  # Set role to 'writer'
                    'emailAddress': i,
                    'transferOwnership': True  # Use transferOwnership=True
                }
            ).execute()
    print(f"Google Sheets document '{sheet_name}' created. URL: {sh.url}")




    return str(sh.url)

if __name__ == "__main__":
    create_google_sheet("Test123", ['judahstarkenburg@gmail.com'])
