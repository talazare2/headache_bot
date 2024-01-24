import pandas as pd
import numpy as np
import math

import seaborn as sns

from reportlab.pdfgen import canvas

path_to_report =  '/home/tiana/Desktop/mathshub_projects/headache_bot/tg_bot_template/report/'
df_test = pd.read_csv(f'{path_to_report}test_db.csv')

sns.relplot(data=df_test, x="date", y="halvl", hue="alc")

# Create a new PDF document
pdf = canvas.Canvas(f'{path_to_report}report_ru.pdf')

# Write the report title
pdf.setFont("Helvetica-Bold", 16)
pdf.drawString(50, 750, "Отчет о головных болях пользователя")

# Write the report content
pdf.setFont("Helvetica", 12)
y = 700
pdf.drawString(50, y, "Name: ")

# Save the PDF document
pdf.save()