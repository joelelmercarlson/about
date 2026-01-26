# /// script
# requires-python = ">=3.12"
# dependencies = [
#     "fpdf>=1.7.2",
# ]
# ///
from fpdf import FPDF

def txt_file_to_pdf(txt_path, pdf_path):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    with open(txt_path, "r") as f:
        for line in f:
            pdf.multi_cell(0, 10, line)

    pdf.output(pdf_path)

txt_file_to_pdf("input.txt", "output.pdf")
