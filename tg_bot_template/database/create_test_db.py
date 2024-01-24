################################
# code to crete test dataframe #
#     similar to real data     #
#      for period PERIOD       #
################################

import pandas as pd
import random as rd
from datetime import date
from dateutil.parser import parse

PERIOD = 30
path_to_db =  '/home/tiana/Desktop/mathshub_projects/headache_bot/tg_bot_template/database/'


columns = [
    'user_id', 'lang', 'date', 
    'halvl', 'loc', 'side', 'alc', 
    'ad', 'fever', 'sleep', 
    't_max', 't_min', 'precip', 
    'wind_force', 'wind_dir' 
    ]

df_test = pd.DataFrame(columns = columns)

def set_new_date(date):
    date_num = list(map(int, date.split('-')))
    year = date_num[0]
    month = date_num[1]
    day = date_num[2]
    try:
        date_num_new = f'{year}-{month}-{day+1}'
        parse(date_num_new)
    except:
        try:
            date_num_new = f'{year}-{month+1}-{1}'
            parse(date_num_new)
        except:
            date_num_new = f'{year+1}-{1}-{1}'
    return date_num_new

def set_ad():
    asyst = rd.randrange(105, 150)
    dif = rd.randrange(35, 55)
    dyast = asyst - dif
    ad = f'{asyst}/{dyast}'
    return ad

row_dict = {}
for i in range(PERIOD):
    row_dict['user_id'] = 'test_id'
    row_dict['lang'] = 'ru'
    if i == 0:
        row_dict['date'] = str(date.today())
    else:
        row_dict['date'] = set_new_date(df_test.iloc[i - 1]['date'])
    row_dict['halvl'] = rd.randrange(6)
    if row_dict['halvl'] == 0:
        row_dict['loc'] = 'NaN'
        row_dict['side'] = 'NaN'
    else:
        row_dict['loc'] = rd.randrange(1, 7)
        row_dict['side'] = rd.choice(['Левая сторона', 'Правая сторона', 'С обеих сторон'])
    row_dict['alc'] = rd.randrange(2)  
    row_dict['ad'] = set_ad()
    row_dict['fever'] = rd.randrange(3)
    row_dict['sleep'] = rd.randrange(6)
    row_dict['t_max'] = round(rd.uniform(5, 16), 2)
    row_dict['t_min'] = round(rd.uniform(-10, 8), 2)
    row_dict['precip'] = rd.randrange(5)
    row_dict['wind_force'] = rd.randrange(3) 
    row_dict['wind_dir'] = rd.randrange(8)
    df_test = pd.concat([df_test,pd.DataFrame([row_dict])], ignore_index=True)
    
df_test.to_csv(f'{path_to_db}test_db.csv', index=False)