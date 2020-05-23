#!/usr/bin/env python3.8

#uses data extracted from chlorophyll fluorescence readings to generate a line graph of each datapoint, as well as generate a rolling mean

import os
import datetime
import pandas as pd
import numpy
import matplotlib.pyplot as plt


data  = pd.read_csv('data/pringlei_13.02.20_infiltration5mM.txt') #name of file from where the data to graph will be extracted
df = pd.DataFrame(data) #makes a dataframe with the file data

#depending on if the data was saved in 2 or 3 columns, one of the next lines is used. Silence the other one by adding a '#' at the start
df.columns = ['time','F','nothing'] #if 3 columns
#df.columns = ['time','F'] #if 2 columns


rolling_mean3 = df.F.rolling(window=50).mean() #generatest the rolling mean as the average of 50 datapoints
df['rolling_mean3']= rolling_mean3 #defines name of the rolling mean

print(df.head()) #prints headings to ensure it is all working properly

df.plot(x='time', y=['F','rolling_mean3'], label=['noisy','50dp']) #makes the plot and graphs both the raw data and the rolling mean

plt.show() #shows plot
