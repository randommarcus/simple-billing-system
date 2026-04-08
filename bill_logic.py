def calculate_item_total(price, quantity):
    return price * quantity


def calculate_subtotal(products):
    subtotal = 0
    for product in products:
        subtotal += product["total"]
    return subtotal


def apply_discount(subtotal):
    """
    Discount Rules:
    - If subtotal >= 1000 → 10% discount
    - If subtotal >= 500 → 5% discount
    - Else → no discount
    """
    if subtotal >= 1000:
        discount = subtotal * 0.10
        discount_label = "10% Discount Applied"
    elif subtotal >= 500:
        discount = subtotal * 0.05
        discount_label = "5% Discount Applied"
    else:
        discount = 0
        discount_label = "No Discount"

    final_total = subtotal - discount
    return discount, final_total, discount_label