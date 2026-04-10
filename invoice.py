def generate_invoice_text(customer_name, invoice_number, bill_datetime, products,
                          subtotal, discount, tax, final_total, discount_label):

    lines = []

    lines.append("=" * 50)
    lines.append("        STORE - INVOICE")
    lines.append("=" * 50)
    lines.append(f"Customer: {customer_name}")
    lines.append(f"Invoice : {invoice_number}")
    lines.append(f"Date    : {bill_datetime}")
    lines.append("-" * 50)

    for p in products:
        lines.append(f"{p['name']} ({p['quantity']} x {p['price']}) = {p['total']}")

    lines.append("-" * 50)
    lines.append(f"Subtotal       : ₹{subtotal:.2f}")
    lines.append(f"{discount_label:<15}: -₹{discount:.2f}")
    lines.append(f"GST (18%)      : +₹{tax:.2f}")
    lines.append(f"Final Total    : ₹{final_total:.2f}")
    lines.append("=" * 50)

    return "\n".join(lines)