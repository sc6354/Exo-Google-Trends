import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt 
import os 
import csv 
os.chdir("/Users/susanchen/Desktop/ExoGoogleTrends")

### reading csv as dataframe
datapath = ("/Users/susanchen/Desktop/ExoGoogleTrends/normalizedExo.csv")
df = pd.read_csv(datapath)
df.rename(columns={"Unnamed: 0" : 'Time', "Exo Kris": "Kris", "Exo Chen": "Chen",
                   "Exo Suho": "Suho", "Exo Tao": "Tao", "Exo Kai": "Kai", "Exo Lay": "Lay"}, inplace= True)


### Plot 1 interest over time
plt.rcParams.update({'font.size': 22})
plt.rcParams['axes.titlepad'] = 30
plot1 = df.plot.line(x= 0, title = "Google Search Interest of EXO since 2012", fontsize= 20, figsize = (22,12), linewidth = 5, colormap = "tab20", grid = True)

plot1.set(ylabel= 'Search Interest')
plot1.title.set_size(30)
plot1.legend(loc=1,fontsize=16)
plt.savefig("plot1.png")



### Plot 2 Ave. interest
from pylab import *
cmap = cm.get_cmap('tab20', 12)    # PiYG
colors =[ ] 
for i in range(cmap.N):
    rgb = cmap(i)[:3] 
    colors.append(matplotlib.colors.rgb2hex(rgb))

plt.rcParams['axes.titlepad'] = 20
plot2 = df.mean().plot.barh(align = "center", alpha = 0.9, figsize = (15, 9), title = "Average Search Interest", color= colors)
for i, v in enumerate(df.mean()):
    plot2.text(v+1, i-.1, str(round(v, 2)),fontweight='bold', fontsize = 18)
plt.xlabel('Average popularity')

plot2.spines["right"].set_visible(False)
plot2.spines["top"].set_visible(False)
plt.savefig("plot2.png")


### Plot 3 Interest Over Time in South Korea
datapath = ("/Users/susanchen/Desktop/ExoGoogleTrends/normalizedSKExo.csv")
df2 = pd.read_csv(datapath)

plt.rcParams.update({'font.size': 22})
plt.rcParams['axes.titlepad'] = 30
plot3 = df2.plot.line(x= 0, title = "Google Search Interest of EXO in S.Korea since 2012", fontsize= 20, figsize = (22,12), linewidth = 5, colormap = "tab20", grid = True)

plot3.set(ylabel= 'Search Interest')
plot3.title.set_size(30)
plot3.legend(loc=2,fontsize=16)

plt.savefig("plot3.png")


### Plot 4 Average Interest in South Koreaplt.rcParams['axes.titlepad'] = 20
plot4 = df2.mean().plot.barh(align = "center", alpha = 0.9, figsize = (15, 9), title = "Average Search Interest in South Korea", color= colors)
for i, v in enumerate(df2.mean()):
    plot4.text(v+1, i-.1, str(round(v, 2)),fontweight='bold', fontsize = 18)
plt.xlabel('Average popularity')

plot4.spines["right"].set_visible(False)
plot4.spines["top"].set_visible(False)
plt.savefig("plot4.png")


### Plot 5 Countrywise Interest Heatmap
datapath3 = ("/Users/susanchen/Desktop/ExoGoogleTrends/normalizedByRegion.csv")
df3 = pd.read_csv(datapath3)

df3.rename(columns={"geoName" : 'Country', "Exo Kris": "Kris", "Exo Chen": "Chen", "Exo Suho": "Suho", "Exo Tao": "Tao", "Exo DO":  "DO", "Exo Kai": "Kai", "Exo Lay": "Lay", "Exo Baekhyun": "Baekhyun"}, inplace= True)
df3.set_index('Country', inplace=True)

zeroRows = (df3 != 0).any(axis=1)
new_df3 = df3.loc[zeroRows] #remove all rows where there is no interest for any member

import seaborn as sns

plt.rcParams['axes.titlepad'] = 20
plt.figure(figsize=(20, 20))

plot5 = sns.heatmap(new_df3, cmap = "YlGnBu", linewidths=0.5, annot_kws={"size": 15},  annot=True)
plot5.set(title = "Exo Members Countrywise Search Levels")
plot5.title.set_size(25)
plot5.set_xticklabels(plot5.get_xmajorticklabels(), fontsize = 18, rotation=45)
plot5.set_yticklabels(plot5.get_ymajorticklabels(), fontsize = 15)
plt.savefig("plot5.png")
