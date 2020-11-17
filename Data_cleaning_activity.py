import pandas as pd
import seaborn as sns
from matplotlib.pyplot import *
import numpy as np

sns.set_theme()

tem = pd.read_csv("CSV_files/second/tempYearly.csv")

rai= pd.read_csv("CSV_files/second/rainYearly.csv")

tem["Rainfall"]=rai["Rainfall"]

med_t = tem["Temperature"].median()

med_r = tem["Rainfall"].median()

cr=0
for i in tem["Rainfall"]:
    try:
        int(i)
    except ValueError:
        tem.loc[cr,"Rainfall"]=med_r
    cr+=1

ct=0
for j in tem["Temperature"]:
    try:
        int(j)
    except ValueError:
        tem.loc[ct,"Temperature"]=med_t
    ct+=1

sns.regplot(x="Rainfall",y="Temperature",data=tem[(0.0 <= tem['Rainfall']) & (tem['Rainfall'] < 10.0) & (0.0 <= tem['Temperature']) & (tem['Temperature'] < 50.0)]) 

show()
