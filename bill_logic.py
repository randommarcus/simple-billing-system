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
    elif subtotal >= 500:
        discount = subtotal * 0.05
    else:
        discount = 0

    final_total = subtotal - discount
    return discount, final_total