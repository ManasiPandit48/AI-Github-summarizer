# utils/export_utils.py
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import pandas as pd

def generate_pdf_report(data, filename="report.pdf"):
    c = canvas.Canvas(filename, pagesize=letter)
    y = 750
    for key, value in data.items():
        c.drawString(50, y, f"{key}: {value}")
        y -= 20
    c.save()

def generate_excel_report(data, filename="report.xlsx"):
    df = pd.DataFrame(list(data.items()), columns=["Metric", "Value"])
    df.to_excel(filename, index=False)