from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.lib import colors
from reportlab.platypus import Paragraph, SimpleDocTemplate, Image
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.pagesizes import A4
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.units import inch, cm
#from report.request import user_id
#from analyzer import headache_lw, headache_max_lw 

path_to_report =  '/home/tiana/Desktop/mathshub_projects/headache_bot/tg_bot_template/report/'
path_to_img =  '/home/tiana/Desktop/mathshub_projects/headache_bot/tg_bot_template/images/'

styles = getSampleStyleSheet() # дефолтовые стили
# the magic is here
styles['Normal'].fontName='DejaVuSerif'
styles['Heading1'].fontName='DejaVuSerif'
styles['Heading2'].fontName='DejaVuSerif'
pdfmetrics.registerFont(TTFont('DejaVuSerif','DejaVuSerif.ttf', 'UTF-8'))


# Create a new PDF document
report = SimpleDocTemplate(f'{path_to_report}report_user_id={123}.pdf',
                        pagesize = A4,
                        title='Отчет о головных болях пользователя',
                        author='Headache-checker_bot')

story = []

story.append(Paragraph(f'Отчет о головных болях пользователя', styles["Heading1"]))

story.append(Paragraph(f'За прошедшую неделю, вы страдали от головной боли : {4} дня (дней), ', styles["Normal"]))
story.append(Paragraph(f'при уровне головной боли выше среднего: {3} дня (дней)', styles["Normal"]))

story.append(Paragraph(f'Распределение головных болей по датам', styles["Heading2"]))

img= Image(f'{path_to_report}img/hl_plot.png')
img.drawHeight =  9*cm
img.drawWidth = 12*cm
story.append(img)

story.append(Paragraph(f'Недельная динамика головных болей', styles["Heading2"]))

img= Image(f'{path_to_report}img/hl_week.png')
img.drawHeight =  9*cm
img.drawWidth = 12*cm
story.append(img)

story.append(Paragraph(f'Распределение головных болей по датам c учетом негативных факторов', styles["Heading2"]))
story.append(Paragraph(f'Употребление алкоголя', styles["Normal"]))
img= Image(f'{path_to_report}img/hlvl_plot_alc.png')
img.drawHeight =  7*cm
img.drawWidth = 10*cm
story.append(img)
story.append(Paragraph(f'Повышенная температура', styles["Normal"]))
img= Image(f'{path_to_report}img/hlvl_plot_fev.png')
img.drawHeight =  7*cm
img.drawWidth = 10*cm
story.append(img)

story.append(Paragraph(f'Качество сна', styles["Normal"]))
img= Image(f'{path_to_report}img/hlvl_plot_sleep.png')
img.drawHeight =  7*cm
img.drawWidth = 10*cm
story.append(img)
img= Image(f'{path_to_report}img/hlvl_sleep.png')
img.drawHeight =  9*cm
img.drawWidth = 10*cm
story.append(img)

story.append(Paragraph(f' Распределение локализации головных болей', styles["Heading2"]))
story.append(Paragraph(f'*Цифровые коды локализации', styles["Normal"]))
img= Image(f'{path_to_img}headache.png')
img.drawHeight =  9*cm
img.drawWidth = 9*cm
story.append(img)
img= Image(f'{path_to_report}img/hlvl_loc.png')
img.drawHeight =  8*cm
img.drawWidth = 19*cm
story.append(img)

story.append(Paragraph(f'Влияние артериального давления на головные боли', styles["Heading2"]))
img= Image(f'{path_to_report}img/hlvl_ad.png')
img.drawHeight =  9*cm
img.drawWidth = 19*cm
story.append(img)

story.append(Paragraph(f'Влияние факторов окружающей среды на головные боли', styles["Heading2"]))
story.append(Paragraph(f'Температура воздуха', styles["Normal"]))
img= Image(f'{path_to_report}img/hlvl_t.png')
img.drawHeight =  9*cm
img.drawWidth = 19*cm
story.append(img)

story.append(Paragraph(f'Метеоусловия:', styles["Normal"]))
story.append(Paragraph(f'0: скорее ясно, 1: скорее пасмурно, 2: дождь, 3: снег, 4: гроза', styles["Normal"]))
img= Image(f'{path_to_report}img/hlvl_meteo.png')
img.drawHeight =  10*cm
img.drawWidth = 11*cm
story.append(img)

story.append(Paragraph(f'Скорость и направление ветра.', styles["Normal"]))
story.append(Paragraph(f'Сила ветра = 0 : слабый ветер. Сила ветра = 1 : умеренный ветер. Сила ветра = 2 : сильный ветер. ', styles["Normal"]))
img= Image(f'{path_to_report}img/wind_sns.png')
img.drawHeight =  8*cm
img.drawWidth = 18*cm
story.append(img)

# Save the PDF document
report.build(story)