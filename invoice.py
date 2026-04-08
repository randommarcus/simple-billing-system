def print_invoice(products, subtotal, discount, final_total):
    print("\n" + "=" * 35)
    print("         FINAL INVOICE")
    print("=" * 35)

    print(f"{'Product':<12}{'Price':<8}{'Qty':<6}{'Total'}")
    print("-" * 35)

    for product in products:
        print(f"{product['name']:<12}{product['price']:<8}{product['quantity']:<6}{product['total']}")

    print("-" * 35)
    print(f"{'Subtotal':<26}₹{subtotal:.2f}")
    print(f"{'Discount':<26}₹{discount:.2f}")
    print(f"{'Final Total':<26}₹{final_total:.2f}")
    print("=" * 35)