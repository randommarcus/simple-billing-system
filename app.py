import streamlit as st
import pandas as pd

from bill_logic import calculate_item_total, calculate_subtotal, apply_discount
from invoice import generate_invoice_text, save_invoice_to_file
from utils import generate_invoice_number, get_current_datetime, ensure_invoice_folder_exists

# Page settings
st.set_page_config(
    page_title="Simple Billing System",
    page_icon="🧾",
    layout="centered"
)

st.title("🧾 Simple Billing System")
st.subheader("Shop/Store Billing Web App")

st.markdown("---")

# Ensure invoice folder exists
ensure_invoice_folder_exists()

# Customer details
customer_name = st.text_input("Enter Customer Name")

st.markdown("## Product Details")

num_products = st.number_input(
    "Enter Number of Products",
    min_value=1,
    max_value=20,
    value=1,
    step=1
)

products = []

for i in range(num_products):
    st.markdown(f"### Product {i + 1}")

    col1, col2, col3 = st.columns(3)

    with col1:
        name = st.text_input(f"Product Name {i + 1}", key=f"name_{i}")

    with col2:
        price = st.number_input(
            f"Price {i + 1}",
            min_value=0.0,
            step=1.0,
            format="%.2f",
            key=f"price_{i}"
        )

    with col3:
        quantity = st.number_input(
            f"Quantity {i + 1}",
            min_value=1,
            step=1,
            key=f"qty_{i}"
        )

    total = calculate_item_total(price, quantity)

    products.append({
        "name": name,
        "price": price,
        "quantity": quantity,
        "total": total
    })

st.markdown("---")

if st.button("Generate Invoice"):
    if not customer_name.strip():
        st.error("Please enter customer name.")
    elif any(not product["name"].strip() for product in products):
        st.error("Please enter all product names.")
    else:
        invoice_number = generate_invoice_number()
        bill_datetime = get_current_datetime()

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

        # Show summary
        st.success("Invoice generated successfully!")

        st.markdown("## Billing Summary")

        summary_df = pd.DataFrame(products)
        summary_df["price"] = summary_df["price"].map(lambda x: f"₹{x:.2f}")
        summary_df["total"] = summary_df["total"].map(lambda x: f"₹{x:.2f}")

        st.dataframe(summary_df, use_container_width=True)

        col1, col2, col3 = st.columns(3)
        col1.metric("Subtotal", f"₹{subtotal:.2f}")
        col2.metric("Discount", f"₹{discount:.2f}")
        col3.metric("Final Total", f"₹{final_total:.2f}")

        st.markdown("## Invoice Preview")
        st.code(invoice_text)

        # Save invoice
        file_path = save_invoice_to_file(invoice_number, invoice_text)

        # Download button
        st.download_button(
            label="📥 Download Invoice",
            data=invoice_text,
            file_name=f"{invoice_number}.txt",
            mime="text/plain"
        )

        st.info(f"Invoice saved locally at: {file_path}")