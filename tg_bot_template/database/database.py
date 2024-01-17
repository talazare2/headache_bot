import pandas as pd


db = {'halvl':[], 'loc':[], 'alc': [], 'pres': [], 'fev': [], 'sleep': [], 'temp': [], 'meteo': [], 'wind': [], 'kp': [], 'add': []}
df_headache = pd.DataFrame(data = db)
print(df_headache)