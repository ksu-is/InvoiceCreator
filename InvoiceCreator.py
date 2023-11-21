from datetime import datetime

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
        invoice_text = f"===== Invoice =====\n"
        invoice_text += f"Date: {self.date.strftime('%Y-%m-%d %H:%M:%S')}\n"
        invoice_text += f"Company: {self.company.name}\n"
        invoice_text += f"Address: {self.company.address}\n"
        invoice_text += f"Phone Number: {self.company.phone_number}\n\n"
        invoice_text += f"Customer: {self.customer_name}\n\n"
        invoice_text += "Items:\n"
        total_amount = 0

        for item in self.items:
            item_name, quantity, unit_price = item
            total_item_amount = quantity * unit_price
            total_amount += total_item_amount
            invoice_text += f"{item_name} - Quantity: {quantity}, Unit Price: ${unit_price}, Total: ${total_item_amount}\n"

        invoice_text += f"\nTotal Amount: ${total_amount}\n"
        invoice_text += "==================\n"
        invoice_text += "Thank you for your business. Have a wonderful day!"

        return invoice_text

    def save_invoice(self):
        filename = f"Invoice_{self.date.strftime('%Y%m%d_%H%M%S')}.txt"
        with open(filename, 'w') as file:
            file.write(self.generate_invoice())
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
invoice_text = invoice.generate_invoice()

print("\nInvoice:")
print(invoice_text)

# Save the invoice to a file
filename = invoice.save_invoice()
print(f"Invoice saved to {filename}")
