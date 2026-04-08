# 🧾 Simple Billing System (Streamlit Web App)

A Python-based billing system for a shop/store built using Streamlit.  
This app allows users to enter customer and product details, calculate total bills, apply discounts, preview invoices, and download them.

## 🚀 Features

- Enter customer name
- Add multiple products
- Input price and quantity
- Automatic subtotal calculation
- Discount rules based on bill amount
- Invoice number generation
- Date & time stamp
- Invoice preview
- Download invoice as `.txt`
- Clean browser-based UI using Streamlit

## 💸 Discount Rules

- 10% discount if subtotal >= ₹1000
- 5% discount if subtotal >= ₹500
- No discount below ₹500

## 🛠 Tech Stack

- Python
- Streamlit
- Pandas
- Git
- GitHub

## 📂 Project Structure

```bash
simple-billing-system/
│
├── app.py
├── bill_logic.py
├── invoice.py
├── utils.py
├── invoices/
├── README.md
├── requirements.txt
└── .gitignore