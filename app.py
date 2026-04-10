import streamlit as st
import pandas as pd

from bill_logic import *
from invoice import generate_invoice_text
from utils import *
from pdf_generator import generate_pdf

st.markdown(
    """
    <style>
    .stButton>button {
        background-color: #4CAF50;
        color: white;
        font-size: 16px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.set_page_config(page_title="Billing System", page_icon="🧾")

st.title("🧾 Store Billing System")
st.markdown("---")

customer_name = st.text_input("Customer Name")

num_products = st.number_input("Number of Products", min_value=1, max_value=10, value=1)

products = []

for i in range(num_products):
    st.subheader(f"Product {i+1}")
    col1, col2, col3 = st.columns(3)

    name = col1.text_input("Name", key=f"name{i}")
    price = col2.number_input("Price", min_value=0.0, key=f"price{i}")
    qty = col3.number_input("Qty", min_value=1, key=f"qty{i}")

    total = calculate_item_total(price, qty)

    products.append({
        "name": name,
        "price": price,
        "quantity": qty,
        "total": total
    })

if st.button("Generate Invoice"):
    if not customer_name:
        st.error("Enter customer name")
    else:
        ensure_invoice_folder_exists()

        invoice_number = generate_invoice_number()
        date = get_current_datetime()

        subtotal = calculate_subtotal(products)
        discount, label = apply_discount(subtotal)

        after_discount = subtotal - discount
        tax, final_total = apply_tax(after_discount)

        invoice_text = generate_invoice_text(
            customer_name,
            invoice_number,
            date,
            products,
            subtotal,
            discount,
            tax,
            final_total,
            label
        )

        st.code(invoice_text)

        # PDF generation
        pdf_path = generate_pdf(invoice_number, invoice_text)

        with open(pdf_path, "rb") as f:
            st.download_button(
                "📥 Download PDF Invoice",
                f,
                file_name=f"{invoice_number}.pdf"
            )