import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from scipy.fft import fft,fftfreq
dat1=pd.read_csv("CSV_files/third/2019-01-05_14.50.30 - Copy.csv")
dat2=pd.read_csv("CSV_files/third/2019-01-08_17.36.06.Harsh_run1.csv")
dat3=pd.read_csv("CSV_files/third/2019-01-08_18.57.58Acceleration_Harsh_run2.csv")
dat4=pd.read_csv("CSV_files/third/2019-01-08_19.10.59Acceleration_Abhishek - Copy.csv")
dat5=pd.read_csv("CSV_files/third/2019-01-08_19.10.59Acceleration_Abhishek_run2 - Copy.csv")

def sumc(dat):
    tot=0.0
    pd.to_numeric(dat)
    for i in dat:
            tot += float(i)
    return tot

def sin_wave_gen(df2,freq=0.1):
    df2.drop([0],axis=0,inplace=True)
    time=df2["Time"]
    time1=time.to_numpy()
    rpm=df2["RPM"]
    rpm1=rpm.to_numpy()
    global N, avg_rpm, avg_time
    avg_rpm, avg_time=sumc(rpm1)/len(rpm1), sumc(time1)/len(time1)
    x = np.linspace(0, avg_time, int(avg_rpm * avg_time), endpoint=True)
    frequencies = x * freq
    N = int(avg_rpm*avg_time)
    y = np.sin((2 * np.pi) * frequencies)
    plt.plot(x,y)
    plt.show()
    return x,y 

def fft_plotter(dat):
    x,y=sin_wave_gen(dat)
    yf = fft(y)
    xf = fftfreq(N, 1 / avg_rpm)
    plt.plot(xf, np.abs(yf))
    plt.show()

fft_plotter(dat1)
fft_plotter(dat2)
fft_plotter(dat3)
fft_plotter(dat4)
fft_plotter(dat5)
