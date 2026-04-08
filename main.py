from bill_logic import calculate_item_total, calculate_subtotal, apply_discount
from invoice import generate_invoice_text, print_invoice, save_invoice_to_file
from utils import generate_invoice_number, get_current_datetime, ensure_invoice_folder_exists


def get_positive_number(prompt):
    while True:
        try:
            value = float(input(prompt))
            if value <= 0:
                print("Please enter a value greater than 0.")
            else:
                return value
        except ValueError:
            print("Invalid input. Please enter a number.")


def get_positive_integer(prompt):
    while True:
        try:
            value = int(input(prompt))
            if value <= 0:
                print("Please enter an integer greater than 0.")
            else:
                return value
        except ValueError:
            print("Invalid input. Please enter a whole number.")


def get_non_empty_text(prompt):
    while True:
        value = input(prompt).strip()
        if value:
            return value
        print("This field cannot be empty.")


def main():
    print("=" * 50)
    print("         WELCOME TO STORE BILLING")
    print("=" * 50)

    ensure_invoice_folder_exists()

    customer_name = get_non_empty_text("Enter customer name: ")
    invoice_number = generate_invoice_number()
    bill_datetime = get_current_datetime()

    products = []

    num_products = get_positive_integer("Enter number of products: ")

    for i in range(num_products):
        print(f"\nEnter details for Product {i + 1}")
        name = get_non_empty_text("Product name: ")
        price = get_positive_number("Price: ₹")
        quantity = get_positive_integer("Quantity: ")

        total = calculate_item_total(price, quantity)

        products.append({
            "name": name,
            "price": price,
            "quantity": quantity,
            "total": total
        })

    subtotal = calculate_subtotal(products)
    discount, final_total, discount_label = apply_discount(subtotal)

    invoice_text = generate_invoice_text(
        customer_name,
        invoice_number,
        bill_datetime,
        products,
        subtotal,
        discount,
        final_total,
        discount_label
    )

    print_invoice(invoice_text)

    file_path = save_invoice_to_file(invoice_number, invoice_text)
    print(f"\nInvoice saved successfully at: {file_path}")


if __name__ == "__main__":
    main()