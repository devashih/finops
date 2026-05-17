from reportlab.pdfgen import canvas

pdf = canvas.Canvas(
    "finops_report.pdf"
)

pdf.drawString(
    100,
    750,
    "LendFlow FinOps Executive Report"
)

pdf.drawString(
    100,
    720,
    "Estimated Savings: $60,000/month"
)

pdf.save()

print("PDF Report Generated")
