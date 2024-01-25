import pandas as pd
import numpy as np
import math
import os

import seaborn as sns
import matplotlib.pyplot as plt

from config_data.paths import path_to_db, path_to_report
from report.request import user_id

os.mkdir(path_to_report, str(user_id))

path_to_report = path_to_report + str(user_id) + '/' 
#df = pd.read_csv(f'{path_to_report}test_db.csv')
df = pd.read_csv(f'{path_to_db}test_db.csv')
#df = pd.read_csv(f'{path_to_db}db.csv')

df = df[df['user_id'] == user_id]

def convert_date(date):
    date_num = list(map(int, date.split('-')))
    year = date_num[0]
    month = date_num[1]
    day = date_num[2]
    year -= 2000
    if month < 10:
        month = f'0{month}'
    date_new = f'{day}.{month}'
    return date_new


def fix_df_date(df):
    df_temp = []
    for _, row in df.iterrows():
        row['date'] = convert_date(row['date'])
        try:
            asyst, dyast = list(map(int, row['ad'].split('/')))
            row['asyst'] = asyst
            row['dyast'] = dyast
        except:
            row['asyst'] = 'NaN'
            row['dyast'] = 'NaN'
        df_temp.append(row)
    df = pd.DataFrame(df_temp)
    return df


def count_data_week(df):
    n=7
    list_df = [df[i:i+n] for i in range(0,len(df),n)]
    ha_list = []
    ha_max_list = []
    for df_chunk in list_df:
        if len(df_chunk) < 7:
            pass
        else:
            ha_list.append(len(df_chunk[df_chunk['halvl'] > 0]))
            ha_max_list.append(len(df_chunk[df_chunk['halvl'] > 3]))
    return ha_list, ha_max_list

df_test=fix_df_date(df)
df_test.sort_values('date', ascending=True)

# Weekly dynamic
ha_list, ha_max_list = count_data_week(df_test)
headache_lw = ha_list[-1]
headache_max_lw = ha_max_list[-1]
fig, ax = plt.subplots()
ax.plot(range(len(ha_list)), ha_list,  color = 'blue')
ax.plot(range(len(ha_max_list)), ha_max_list,  color = 'red')
ax.legend(['Любой уровень головной боли', 'Сильная головная боль'])
ax.set_title('Динамика головной боли по неделям')
ax.set_xlabel("Неделя")
ax.set_ylabel("Дни головной боли")
fig.savefig(f'{path_to_report}/img/hl_week.png')
fig.clear()

# Headache level by days
sns.set(rc = {'figure.figsize':(20,8)})
sns.set(font_scale=1)
hlvl_pl = sns.barplot(data=df_test, x="date", y="halvl", hue = None)
hlvl_pl.set_xticks(hlvl_pl.get_xticks()[::4])
hlvl_pl.set_xlabel("Дата")
hlvl_pl.set_ylabel("Уровень головной боли")
hlvl_pl.figure.savefig(f'{path_to_report}/img/hl_plot.png')
hlvl_pl.figure.clear()

# Headache level by days with alcohol
hlvl_plot_alc = sns.barplot(data=df_test, x="date", y="halvl", hue="alc")
leg = hlvl_plot_alc.get_legend()
new_title = 'Алкоголь накануне'
leg.set_title(new_title)
new_labels = ['Нет', 'Да' ]
for t, l in zip(leg.texts, new_labels):
    t.set_text(l)
hlvl_plot_alc.set_xlabel("Дата")
hlvl_plot_alc.set_xticks(hlvl_plot_alc.get_xticks()[::4])
hlvl_plot_alc.set_ylabel("Уровень головной боли")
hlvl_plot_alc.figure.savefig(f'{path_to_report}/img/hlvl_plot_alc.png')
hlvl_plot_alc.figure.clear()

# Headache level by days with fever
hlvl_plot_fev = sns.barplot(data=df_test, x="date", y="halvl", hue="fever", palette='deep')
leg = hlvl_plot_fev.get_legend()
new_title = 'Температура'
leg.set_title(new_title)
new_labels = ['Нормальная', 'Повышенная', 'Высокая' ]
for t, l in zip(leg.texts, new_labels):
    t.set_text(l)
hlvl_plot_fev.set_xlabel("Дата")
hlvl_plot_fev.set_xticks(hlvl_plot_fev.get_xticks()[::4])
hlvl_plot_fev.set_ylabel("Уровень головной боли")
hlvl_plot_fev.figure.savefig(f'{path_to_report}/img/hlvl_plot_fev.png')
hlvl_plot_fev.figure.clear()

# Headache level by days as sleep quality
hlvl_plot_sleep = sns.barplot(data=df_test, x="date", y="halvl", hue="sleep", palette='deep')
leg = hlvl_plot_sleep.get_legend()
new_title = 'Качество сна'
leg.set_title(new_title)
hlvl_plot_sleep.set_xlabel("Дата")
hlvl_plot_sleep.set_xticks(hlvl_plot_sleep.get_xticks()[::4])
hlvl_plot_sleep.set_ylabel("Уровень головной боли")
hlvl_plot_sleep.figure.savefig(f'{path_to_report}/img/hlvl_plot_sleep.png')
hlvl_plot_sleep.figure.clear()

# Headache level by days as sleep quality
hlvl_sleep = sns.relplot(data=df_test, x="sleep", y="halvl")
hlvl_sleep.ax.set_xlabel("Качество сна")
hlvl_sleep.ax.set_ylabel("Уровень головной боли")
hlvl_sleep.figure.savefig(f'{path_to_report}/img/hlvl_sleep.png')
hlvl_sleep.figure.clear()

# Headache level by days as meteoconditions
hlvl_meteo = sns.relplot(data=df_test, x="precip", y="halvl")
hlvl_meteo.ax.set_xlabel("Метеоусловия")
hlvl_meteo.ax.set_ylabel("Уровень головной боли")
hlvl_meteo.figure.savefig(f'{path_to_report}/img/hlvl_meteo.png')
hlvl_meteo.figure.clear()

# Headache level by days and blood pressure

sns.set_theme(style = 'ticks')
sns.set_style("white")
sns.set_context("talk") 

hlvl_ad, ax1 = plt.subplots()
ax2 = ax1.twinx() 
sns.lineplot(data=df_test, x="date", y="asyst", ax = ax1, color='darksalmon')
sns.lineplot(data=df_test, x="date", y="dyast",ax = ax1, color='steelblue')
sns.scatterplot(data=df_test, x="date", y="halvl", ax = ax2, color='darkred')
ax1.set_xlabel("Дата")
ax1.set_xticks(ax1.get_xticks()[::4])
ax1.set_ylabel("Артериальное давление")
ax2.set_ylabel("Уровень головной боли")
hlvl_ad.savefig(f'{path_to_report}/img/hlvl_ad.png')
hlvl_ad.clear()

# Headache level by days and temperature

hlvl_t, ax1 = plt.subplots()
ax2 = ax1.twinx() 
sns.lineplot(data=df_test, x="date", y="t_max", ax = ax1, color='darksalmon')
sns.lineplot(data=df_test, x="date", y="t_min",ax = ax1, color='steelblue')
sns.scatterplot(data=df_test, x="date", y="halvl", ax = ax2, color='darkred')
ax1.set_xlabel("Дата")
ax1.set_xticks(ax1.get_xticks()[::4])
ax1.set_ylabel("Температура воздуха")
ax2.set_ylabel("Уровень головной боли")
hlvl_t.savefig(f'{path_to_report}/img/hlvl_t.png')
hlvl_t.clear()


# headache localisation
df_loc = df_test[['halvl', 'loc', 'side']]
loc = sns.relplot(
    data=df_loc,
    x="loc", y="halvl", col="side", hue="side",
    palette="deep", zorder=5, legend=False,
)
for side, axis in loc.axes_dict.items():
    axis.set_title(side)
    axis.set_xlabel("Локализация боли")
    axis.set_ylabel("Уровень боли")

loc.figure.savefig(f'{path_to_report}/img/hlvl_loc.png')
loc.figure.clear()

df_w = df_test[['halvl', 'wind_force','wind_dir_ex']]

#fig, ax = plt.subplots(ncols=3, subplot_kw={'projection':'polar'})
#df = df_w.set_index(['wind_force','wind_dir_ex'])
#ldf_1 = df.loc[0]
#x = ldf_1.index / 180 * 3.14159 
#y = ldf_1.halvl
#ax[0].plot(x, y, "o")
#ldf_2 = df.loc[1]
#x = ldf_2.index / 180 * 3.14159
#y = ldf_2.halvl
#ax[1].plot(x, y, "o")
#ldf_3 = df.loc[2]
#x = ldf_3.index / 180 * 3.14159
#y = ldf_3.halvl
#ax[2].plot(x, y, "o")
#for axi in ax:
#    axi.set_theta_offset(math.pi/2)
#    axi.set_xlabel('Wind direction')
#fig.savefig(f'{path_to_report}/img/wind.png')

g = sns.FacetGrid(df_w, col="wind_force", hue="wind_force",
                  subplot_kws=dict(projection='polar'), height=4.5,
                  sharex=False, sharey=False, despine=False)
g.map(sns.scatterplot, "wind_dir_ex", "halvl")
for wf, ax in g.axes_dict.items():
    ax.set_title(f'Сила ветра = {wf}')
    ax.title.set_position([.5, 1.1])
    ax.yaxis.labelpad = 40
    ax.set_ylabel('')
    ax.set_xlabel('')
    ax.set_theta_offset(math.pi/2)
    ax.set_xticklabels(['N', 'NW', 'W', "SW", 'S', 'SE', 'E', 'NE'])

g.figure.savefig(f'{path_to_report}/img/wind_sns.png')
g.figure.clear()
