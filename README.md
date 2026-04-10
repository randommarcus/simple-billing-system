# 🧾 Simple Billing System Web App

A professional billing system built using Python and Streamlit that allows users to generate invoices, apply discounts, calculate GST, and download invoices as PDF files.

---

## 🚀 Features

* Enter customer details
* Add multiple products
* Automatic subtotal calculation
* Discount logic:

  * 10% discount for ₹1000+
  * 5% discount for ₹500+
* GST (18%) calculation
* Real-time invoice preview
* Download invoice as PDF
* Unique invoice number generation
* Date & time stamping
* Clean and user-friendly web interface

---

## 💸 Pricing Logic

* Subtotal = Sum of all product totals
* Discount applied based on subtotal
* GST (18%) applied after discount
* Final Total = (Subtotal - Discount) + GST

---

## 💻 Tech Stack

* Python
* Streamlit
* Pandas
* ReportLab (PDF generation)
* Git & GitHub

---

## 📂 Project Structure

```bash
simple-billing-system/
│
├── app.py                     # Streamlit web app
├── bill_logic.py              # Billing + GST logic
├── invoice.py                 # Invoice formatting
├── utils.py                   # Utility functions
├── pdf_generator.py           # PDF invoice generation
├── assets/
│   └── fonts/
│       └── DejaVuSans.ttf     # Unicode font for ₹ support
├── invoices/                  # Generated invoices (ignored in Git)
├── requirements.txt
├── README.md
└── .gitignore
```

---

## ⚙️ Installation & Setup

1. Clone the repository:

git clone https://github.com/yourusername/simple-billing-system.git
cd simple-billing-system

2. Install dependencies:

pip install -r requirements.txt

3. Run the application:

streamlit run app.py

---

## 🧪 Sample Test Case

Customer Name: Riya

Products:

| Product | Price | Quantity |
| ------- | ----- | -------- |
| Soap    | 40    | 3        |
| Shampoo | 120   | 5        |

### Expected Output

* Subtotal: ₹720
* Discount (5%): ₹36
* After Discount: ₹684
* GST (18%): ₹123.12
* Final Total: ₹807.12

---

## 📄 PDF Invoice Support

* Invoices are generated using ReportLab
* Unicode support added for ₹ symbol using custom font
* Downloadable directly from the web app
* Stored locally in the `invoices/` folder

---
