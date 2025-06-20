from fpdf import FPDF
import pandas as pd


pdf = FPDF(orientation='P', unit='mm', format='A4')

df = pd.read_csv("topics.csv")

for index, row in df.iterrows():
    topic = row['Topic']
    pages = int(row['Pages'])

    pdf.add_page()

    pdf.set_font(family="Times", style="B", size=12)
    pdf.set_text_color(100, 100, 100)
    pdf.cell(w=0, h=12, txt=topic, align='L', ln=1)
    pdf.line(10, 20, 200, 22)
    for i in range(pages-1):
        pdf.add_page()

pdf.output('topics_generated.pdf')