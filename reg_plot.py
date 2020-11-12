import seaborn as sns
import pandas as pd
from matplotlib.pyplot import *

sns.set_theme()

dat = pd.read_csv("tempYearly.csv")

sns.lineplot(x="Year", y="Temperature", data=dat)
    
show()
