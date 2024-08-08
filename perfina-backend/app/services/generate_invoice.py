from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Image, Spacer
from reportlab.lib.units import inch
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
import io

def generate_invoice(
    company_name, company_address, company_postal_code, company_phone, company_email,
    company_ico, company_dic, company_bank_account, category, services, rate, hours,
    invoice_number, variable_symbol, invoice_date, invoice_due,
    client_name, client_address, client_postal_code, client_ico, client_dic
):
    def merge_info(info_list):
        return "\n".join(info_list)

    new_service = ['Služby', 'Popis práce', 'Smluvní cena', 'Počet hodin', 'Celkem']
    
    total_amount = f"{round(hours * rate)} Kč"

    billing_info = ["Odběratel:", client_name, client_address, client_postal_code, "", f"IČO: {client_ico}", f"DIČ: {client_dic}"]

    company_info = [
        "Dodavatel:", company_name, company_address, company_postal_code,
        "", "", company_email, company_phone, "", "",
        f"IČO: {company_ico}", f"DIČ: {company_dic}", company_bank_account,
        "", "", f"Číslo faktury: {invoice_number}", "",
        f"Datum vystavení: {invoice_date}", f"Datum splatnosti: {invoice_due}",
        f"Variabilní symbol: {variable_symbol}",
    ]

    billing_services = [
        new_service,
        [category, services, f"{rate} Kč/h", hours, total_amount],
    ]

    # Register DejaVuSans font
    pdfmetrics.registerFont(TTFont('DejaVuSans', 'DejaVuSans.ttf',))
    pdfmetrics.registerFont(TTFont('DejaVuSansBold', 'DejaVuSans-Bold.ttf',))

    # Create a custom paragraph style
    styles = getSampleStyleSheet()

    custom_paragraph_style = ParagraphStyle(
        'DejaVuSans',
        parent=styles['Normal'],
        fontName='DejaVuSans',
        fontSize=10,
    )

    table_style = TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
        ('FONTNAME', (0, 0), (-1, -1), 'DejaVuSans'),
    ])

    # Create PDF
    buffer = io.BytesIO()
    doc = SimpleDocTemplate(buffer, pagesize=letter)
    elements = []

    danovy_doklad = Table([["Daňový doklad", ""]], colWidths=[9 * inch, 0.75 * inch], style=[
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('LEFTPADDING', (0, 0), (-1, -1), 120),
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
        ('FONTNAME', (0, 0), (-1, -1), 'DejaVuSans'),
    ])
    elements.append(danovy_doklad)

    elements.append(Image('logo.png', 1.5 * inch, 1.5 * inch))
    elements.append(Spacer(1, 0.25 * inch))

    # Contacts table
    contacts = [[merge_info(company_info), merge_info(billing_info)]]
    contacts_table = Table(contacts, colWidths=[5 * inch, 5 * inch],)
    contacts_table.setStyle(TableStyle([
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('LEFTPADDING', (0, 0), (-1, -1), 120),
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
        ('FONTNAME', (0, 0), (-1, -1), 'DejaVuSans'),
    ]))
    elements.append(contacts_table)
    elements.append(Spacer(1, 0.25 * inch))

    # Services table
    services_table = Table(billing_services, colWidths=[1 * inch, 3 * inch, 1 * inch, 1 * inch, 1 * inch], style=table_style)
    elements.append(services_table)
    elements.append(Spacer(1, 0.25 * inch))

    # Total amount
    total_table = Table([["Celkem k úhradě:", total_amount]], colWidths=[6.5 * inch, 0.75 * inch], style=[
        ('ALIGN', (0, 0), (-1, -1), 'RIGHT'),
        ('FONTNAME', (0, 0), (-1, -1), 'DejaVuSansBold'),
    ])
    elements.append(total_table)

    total_table = Table([["", "Neplátce DPH"]], colWidths=[6.5 * inch, 0.75 * inch], style=[
        ('ALIGN', (0, 0), (-1, -1), 'RIGHT'),
        ('FONTNAME', (0, 0), (-1, -1), 'DejaVuSansBold'),
    ])
    elements.append(total_table)

    elements.append(Spacer(1, 0.25 * inch))
    elements.append(Spacer(1, 0.25 * inch))

    total_table = Table([["", "Vystavil: Vu Michal (jednatel)"]], colWidths=[6.5 * inch, 0.75 * inch], style=[
        ('ALIGN', (0, 0), (-1, -1), 'RIGHT'),
        ('FONTNAME', (0, 0), (-1, -1), 'DejaVuSans'),
    ])
    elements.append(total_table)

    # Build PDF
    doc.build(elements)
    
    buffer.seek(0)
    return buffer
