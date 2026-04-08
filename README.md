# Simple Billing System (Python)

A beginner-friendly Python billing system for a shop/store that allows users to enter product details, calculate totals, apply discounts, and print a final invoice.

## Features

- Add multiple products
- Enter customer name
- Auto-generate invoice number
- Capture date and time of billing
- Enter product name, price, and quantity
- Automatic subtotal calculation
- Conditional discount application
- Clean invoice display in terminal
- Save invoice as `.txt` file
- Input validation for better usability

## Discount Rules

- 10% discount if subtotal >= ₹1000
- 5% discount if subtotal >= ₹500
- No discount below ₹500

## Future Improvements

- GUI using Tkinter
- Web app using Streamlit
- GST/tax calculation
- Product code support
- PDF invoice generation
- Database integration

## Project Structure

```bash
simple-billing-system/
│
├── main.py          # Main program
├── bill_logic.py    # Billing calculations
├── invoice.py       # Invoice printing
├── README.md
├── requirements.txt
└── .gitignore