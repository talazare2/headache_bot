import pandas as pd
from typing import Dict
from config_data.paths import path_to_db

def create_df(usr_dict):
    columns = [
        'user_id', 'lang', 'date', 
        'halvl', 'loc', 'side', 'alc', 
        'ad', 'fever', 'sleep', 
        't_max', 't_min', 'precip', 
        'wind_force', 'wind_dir'
        ]

    df = pd.DataFrame(columns = columns)
    df = pd.concat([df,pd.DataFrame([usr_dict])], ignore_index=True, )

    # append line to CSV file
    df.to_csv(f'{path_to_db}db.csv', mode='a', index=False, header = False)