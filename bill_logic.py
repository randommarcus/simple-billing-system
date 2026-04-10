def calculate_item_total(price, quantity):
    return price * quantity


def calculate_subtotal(products):
    return sum(p["total"] for p in products)


def apply_discount(subtotal):
    if subtotal >= 1000:
        discount = subtotal * 0.10
        label = "10% Discount"
    elif subtotal >= 500:
        discount = subtotal * 0.05
        label = "5% Discount"
    else:
        discount = 0
        label = "No Discount"

    return discount, label


def apply_tax(amount_after_discount):
    GST_RATE = 0.18  # 18% GST
    tax = amount_after_discount * GST_RATE
    final_total = amount_after_discount + tax
    return tax, final_total