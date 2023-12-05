from datetime import datetime
from io import BytesIO
from reportlab.pdfgen import canvas

class Company:
    def __init__(self, name, address, phone_number):
        self.name = name
        self.address = address
        self.phone_number = phone_number

class Invoice:
    def __init__(self, customer_name, items, company):
        self.customer_name = customer_name
        self.items = items
        self.company = company
        self.date = datetime.now()

    def generate_invoice(self):
        buffer = BytesIO()
        p = canvas.Canvas(buffer)
    
        # Header
        p.drawString(100, 800, f"===== Invoice =====")
        p.drawString(100, 780, f"Date: {self.date.strftime('%Y-%m-%d %H:%M:%S')}")
        p.drawString(100, 760, f"Company: {self.company.name}")
        p.drawString(100, 740, f"Address: {self.company.address}")
        p.drawString(100, 720, f"Phone Number: {self.company.phone_number}")
    
        p.drawString(100, 680, f"Customer: {self.customer_name}")
    
        # Items
        p.drawString(100, 640, "Items")
        y_position = 620
        total_amount = 0

        for item in self.items:
            item_name, quantity, unit_price = item
            total_item_amount = quantity * unit_price
            total_amount += total_item_amount

            item_text = f"{item_name} - Quantity: {quantity}, Unit Price: ${unit_price}, Total: ${total_item_amount}"
            p.drawString(100, y_position, item_text)
            y_position -=  20  
        
        # Total Amount
        p.drawString(100, y_position, f"Total Amount: ${total_amount}")

        # Footer
        p.drawString(100, 100, "Thank you for your business. Have a wonderful day!")
        p.drawString(100, 80, "==================")

        p.showPage()
        p.save()

        buffer.seek(0)
        return buffer

    def save_invoice(self):
        filename = f"Invoice_{self.date.strftime('%Y%m%d_%H%M%S')}.pdf"
        buffer = self.generate_invoice()

        with open(filename, 'wb') as file:
            file.write(buffer.getvalue())

        return filename

# Get user input for company details
company_name = input("Enter company name: ")
company_address = input("Enter company address: ")
company_phone_number = input("Enter company phone number: ")

# Get user input for customer and item details
customer_name = input("Enter customer name: ")
items = []

while True:
    item_name = input("Enter item name (or 'done' to finish): ")
    if item_name.lower() == 'done':
        break

    quantity = int(input("Enter quantity: "))
    unit_price = float(input("Enter unit price: "))

    items.append((item_name, quantity, unit_price))

# Create the company and invoice objects
company = Company(company_name, company_address, company_phone_number)
invoice = Invoice(customer_name, items, company)

# Create and display the invoice
invoice_pdf_buffer = invoice.generate_invoice()

# Save the invoice to a file
filename = invoice.save_invoice()
print(f"Invoice saved to {filename}")
