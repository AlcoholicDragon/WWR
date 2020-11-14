import seaborn as sns
import pandas as pd
from matplotlib.pyplot import *

sns.set_theme()

tem = pd.read_csv("CSV_files/first/tempYearly.csv")

rai = pd.read_csv("CSV_files/first/rainYearly.csv")

tem["Rainfall"]=rai["Rainfall"]

sns.regplot(x="Rainfall", y="Temperature", data=tem)
    
show()
