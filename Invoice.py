def invoice_total(items=None):
    net_total: int = sum(item["value"] for item in items)
    gst = net_total * 0.05
    pst = net_total * 0.08
    total = net_total + gst + pst
    return net_total, gst, pst, total


def generate_invoice():
    invoice_number = input("Enter invoice number: ")
    customer_number = input("Enter Customer Number: ")
    customer_name = input("Enter Customer Name: ")

    items = []
    description = input("Enter item description (or 'done' to finish): ")
    value = float(input("Enter item value: "))
    items.append({"description": description, "value": value})

    net, gst, pst, total = invoice_total()

    print("Invoice Number: ", invoice_number)
    print("Customer Number: ", customer_number)
    print("Customer Name: ", customer_name)
    print("-------------------------------")
    print("items with their values:")
    print("Net: ", net)
    print("Gst:", gst)
    print("Pst: ", pst)
    print("Total: ", total)

def main():
    print("Menu:")
    print("1. Generate Invoice")
    print("2. Generate Purchase Order (PO)")
    print("3. Quit")

    choice = input("Enter your choice (1/2/3): ")
    if choice == '1':
        print("Generating Invoice:")
        generate_invoice()
    elif choice == '2':
        print("Generating Purchase Order (PO):")
        generate_invoice()
    elif choice == '3':
        print("Goodbye!")
    else:
        print("Invalid choice. Please enter 1, 2, or 3.")

if __name__ == "__main__":
     main()
