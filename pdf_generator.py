from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.pdfbase import ttfonts
from reportlab.pdfbase import pdfmetrics


def generate_pdf(invoice_number, invoice_text):
    file_path = f"invoices/{invoice_number}.pdf"

    # ✅ Register Unicode font
    font_path = "assets/fonts/DejaVuSans.ttf"
    pdfmetrics.registerFont(ttfonts.TTFont("DejaVu", font_path))

    doc = SimpleDocTemplate(file_path)
    styles = getSampleStyleSheet()

    # Apply custom font
    style = styles["Normal"]
    style.fontName = "DejaVu"

    content = []

    for line in invoice_text.split("\n"):
        content.append(Paragraph(line, style))
        content.append(Spacer(1, 8))

    doc.build(content)

    return file_path