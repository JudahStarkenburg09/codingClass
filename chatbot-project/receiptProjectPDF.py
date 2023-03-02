from fpdf import FPDF
import os
from datetime import datetime
import random

def receiptPrank():

    # current_directory = os.getcwd()
    # folder1 = 'data'
    # os.chdir(os.path.join(current_directory, folder1))

    # Prompt the user for some input
    customer_name = input("Customer name: ")
    cityStateCounty = input("City, Country, and State: ")
    location = input("Address: ")
    price = float(input("Price: "))
    date = input("Date (MM/DD/YYYY): ")
    item = input("Item: ")

    # Create the PDF file
    pdf = FPDF()
    pdf.add_page()
    #add font
    pdf.add_font('Courier New', '', 'cour.ttf', uni=True)
    # Add the receipt header
    pdf.set_font("Courier New", "", 8)
    pdf.cell(0, 10, "     Receipt", 0)
    pdf.cell(0, 10, "", 0, 1)
    # Add the customer and product details

    if len(customer_name) > 18:
        pdf.cell(0, 4, "Customer:  " + customer_name[:18] + "-", ln=1)
        pdf.cell(50, 4, customer_name[18:], ln=1)
        pdf.cell(0, 2, "", 0, 1)
    else:
        pdf.cell(0, 4, "Customer:  " + customer_name, ln=1)

    if len(cityStateCounty) > 18:
        pdf.cell(0, 4, "City:  " + cityStateCounty[:18] + "-", ln=1)
        pdf.cell(50, 4, cityStateCounty[18:], ln=1)
        pdf.cell(0, 2, "", 0, 1)
    else:
        pdf.cell(0, 4, "City:  " + cityStateCounty, ln=1)

    if len(location) > 18:
        pdf.cell(0, 4, "Address:  " + location[:18] + "-", ln=1)
        pdf.cell(50, 4,location[18:], ln=1)
        pdf.cell(0, 2, "", 0, 1)
    else:
        pdf.cell(0, 4, "Address:  " + location, ln=1)

    pdf.cell(50, 4, "Price:  " + "${:.2f}".format(price), ln=1)

    pdf.cell(50, 4, "Date:  " + date, ln=1)

    if len(item) > 18:
        pdf.cell(0, 4, "Item:  " + item[:18] + "-", ln=1)
        pdf.cell(50, 4, item[18:], ln=1)
        pdf.cell(0, 2, "", 0, 1)
        
    else:
        pdf.cell(0, 4, "Item:  " + item, ln=1)
        

    pdf.cell(0, 5, "----------------------------", 0, 1)
    # Add the barcode
    pdf.set_font("Courier New", "", 8)
    pdf.set_font("Courier New", "", 8)
    pdf.cell(50, 6, "██ █ ██ ██ █ ██", 0, 1)
    # Add payment and tax information
    pdf.cell(50, 4, """Purchased on Linus.co""", 0, 1)
    payment_method = random.choice(["cash", "credit", "debit"])
    pdf.cell(50, 4, "Payment with " + payment_method, 0, 1)

    if payment_method == "credit" or payment_method == "debit":
        card_number = str(random.randint(1, 9)) + '*** ' + '**** ' + '****' 
        pdf.cell(50, 4, "Card: " + card_number, 0, 1)

    tax_rate = 0.005  # 0.5%
    tax = price * tax_rate
    total = price + tax
    pdf.cell(50, 5, "Tax (0.5%):" + "${:.2f}".format(tax), 0, ln=1)
    pdf.cell(50, 5, "Total:" + "${:.2f}".format(total), 0, ln=1)

    # Save the PDF file
    pdf_file_name = "receipt.pdf"
    pdf.output(pdf_file_name)
    return "Receipt Created! Check The 'data' Folder For 'receipt.pdf'!"