def generate_invoice_text(customer_name, invoice_number, bill_datetime, products, subtotal, discount, final_total, discount_label):
    lines = []

    lines.append("=" * 50)
    lines.append("              STORE BILLING SYSTEM")
    lines.append("=" * 50)
    lines.append(f"Customer Name : {customer_name}")
    lines.append(f"Invoice Number: {invoice_number}")
    lines.append(f"Date & Time   : {bill_datetime}")
    lines.append("-" * 50)
    lines.append(f"{'Product':<15}{'Price':<10}{'Qty':<8}{'Total'}")
    lines.append("-" * 50)

    for product in products:
        lines.append(
            f"{product['name']:<15}{product['price']:<10.2f}{product['quantity']:<8}{product['total']:.2f}"
        )

    lines.append("-" * 50)
    lines.append(f"{'Subtotal':<35}₹{subtotal:.2f}")
    lines.append(f"{discount_label:<35}₹{discount:.2f}")
    lines.append(f"{'Final Total':<35}₹{final_total:.2f}")
    lines.append("=" * 50)

    return "\n".join(lines)


def save_invoice_to_file(invoice_number, invoice_text):
    file_path = f"invoices/{invoice_number}.txt"
    with open(file_path, "w", encoding="utf-8") as file:
        file.write(invoice_text)
    return file_path