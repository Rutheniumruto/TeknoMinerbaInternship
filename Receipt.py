from reportlab.platypus import Paragraph, SimpleDocTemplate, Table, TableStyle
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet

DATA = [
    ["Date", "Name", "Subscription", "Price(Rp.)"],
    ["30/01/2025", "E-Course : Analisis Data Tambang untuk Mine Analyst", "Lifetime", "186,500.00"],
    ["30/01/2025", "Buku Kualitas Air Sungai Berbantuan Software", "Lifetime", "112,000.00"],
    ["30/01/2025", "Buku Analisa & Perancangan SIstem Informasi Berorientasi Objek", "Lifetime", "115,000.00"],
    ["30/01/2025", "Buku Perancangan Sistem Kendali", "Lifetime", "131,000.00"],
    ["Sub Total", "", "", "544,500.00"],
    ["Diskon", "", "", "4,500.00"],
    ["Total", "", "", "540,000.00"]
    ]
 
pdf = SimpleDocTemplate("TeknoMinerbaPaymentScript.pdf", pagesize = A4)

styles = getSampleStyleSheet()

title_style = styles["Heading1"]

title_style.alignment = 1

title = Paragraph ("Tekno Minerba Receipt", title_style)

style = TableStyle(
    [
        ("BOX", (0,0), (-1,-1), 1, colors.black),
        ("GRID", (0,0), (4,4), 1, colors.black),
        ("BACKGROUND", (0,0), (3,0), colors.darkblue),
        ("TEXTCOLOR", (0,0), (-1,0), colors.white),
        ("ALIGN", (0,0), (-1,-1),"CENTER"),
        ("BACKGROUND", (0,1), (-1,-1), colors.white),
    ]
)

table = Table(DATA, style = style)

pdf.build([title, table])