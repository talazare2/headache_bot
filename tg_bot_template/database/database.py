import pandas as pd
import numpy as np

from day_dict import df_dict

df_cols = np.array(df_dict.keys())
df_list = list(df_dict.values())

print(df_list)
df = pd.DataFrame(columns = df_cols)
