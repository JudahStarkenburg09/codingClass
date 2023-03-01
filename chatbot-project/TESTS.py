from fpdf import FPDF
import os

current_directory = os.getcwd()
folder1 = 'data'
os.chdir(os.path.join(current_directory, folder1))

# Prompt the user for some input
customer_name = input("Customer name: ")
product_name = input("Product name: ")
price = float(input("Price: "))

# Create the PDF file
pdf = FPDF()
pdf.add_page()

#add font
pdf.add_font('Courier New', '', 'cour.ttf', uni=True)

# Add the receipt header
pdf.set_font("Courier New", "", 12)
pdf.cell(0, 10, "Receipt", 0, 1, "C")
pdf.cell(0, 10, "", 0, 1)

# Add the customer and product details
pdf.set_font("Courier New", "", 12)
pdf.cell(50, 10, "Customer name:", 0)
pdf.cell(0, 10, customer_name, 0, 1)

pdf.cell(50, 10, "Product name:", 0)
pdf.cell(0, 10, product_name, 0, 1)

pdf.cell(50, 10, "Price:", 0)
pdf.cell(0, 10, "${:.2f}".format(price), 0, 1)

# Save the PDF file
pdf_file_name = "receipt.pdf"
pdf.output(pdf_file_name)

# Allow the user to download the PDF file
with open(pdf_file_name, "rb") as f:
    pdf_data = f.read()

print("The PDF File Has Been Downloaded! Check The 'Data' Folder For 'receipt.pdf'!")

