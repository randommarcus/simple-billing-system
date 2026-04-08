from datetime import datetime
import os


def generate_invoice_number():
    return datetime.now().strftime("INV%Y%m%d%H%M%S")


def get_current_datetime():
    return datetime.now().strftime("%d-%m-%Y %I:%M:%S %p")


def ensure_invoice_folder_exists():
    if not os.path.exists("invoices"):
        os.makedirs("invoices")