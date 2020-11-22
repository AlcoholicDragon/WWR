import pandas as pd
import seaborn as sns
from matplotlib.pyplot import *
import numpy as np
from random import randint

sns.set_theme()

tem = pd.read_csv("CSV_files/second/tempYearly.csv")

rai= pd.read_csv("CSV_files/second/rainYearly.csv")

tem["Rainfall"]=rai["Rainfall"]

med_t = tem["Temperature"].median()

med_r = tem["Rainfall"].median()

#checking the data type of all entries
for i in tem:
    for j in range(len(tem[i])):
        type(tem[i][j])

#changing two random float data type entries to int
for i in range(2):
    k=randint(1,61)
    int(tem["Rainfall"][k])

#changing Null values (Nan) to median

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

#plotting the graph 

ntem = tem[(0.0 <= tem['Rainfall']) & (tem['Rainfall'] < 10.0) & (0.0 <= tem['Temperature']) & (tem['Temperature'] < 50.0)]

sns.regplot(x="Rainfall",y="Temperature",data=ntem) 

show()
