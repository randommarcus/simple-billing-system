from bill_logic import calculate_item_total, calculate_subtotal, apply_discount
from invoice import print_invoice


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


def main():
    print("=" * 40)
    print("     WELCOME TO STORE BILLING")
    print("=" * 40)

    products = []

    num_products = get_positive_integer("Enter number of products: ")

    for i in range(num_products):
        print(f"\nEnter details for Product {i + 1}")
        name = input("Product name: ").strip()

        while not name:
            print("Product name cannot be empty.")
            name = input("Product name: ").strip()

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
    discount, final_total = apply_discount(subtotal)

    print_invoice(products, subtotal, discount, final_total)


if __name__ == "__main__":
    main()