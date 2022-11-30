#from unittest.mock import inplace

import  pandas as pd
import numpy as np
import  os
import glob
import matplotlib.pyplot as plt
from PIL._imaging import display
from matplotlib.pylab import rcParams
rcParams['figure.figsize']= 10, 6

path = ('C:\\Users\\LENOVO\\PycharmProjects\\Explatory analysis\\data\\')
csv_files = glob.glob(path +"/*.csv")
df_list = (pd.read_csv(file) for file in csv_files)

big_df = pd.concat(df_list, ignore_index= True)
big_df
big_df.info()
big_df=columns = big_df.columns[big_df.dtypes=='str']

#df.dropna(inplace-True)

big_df['DATE'] = pd.to_datetime(big_df['DATE'], infer_datetime_format=True)

indexedDataset = big_df.set_index['DATE']

from datetime import datetime

plt.xlabel("DATE")
plt.ylabel("Volume")
plt.plot(indexedDataset)

#rolling mean
rolmean = indexedDataset.rolling(window =12).mean()

# standard deviation
rolstd = indexedDataset.rolling(window = 12).std()

print(rolstd,rolmean)

#plot rolling stat
orig = plt.plot(indexedDataset, color ='blue', label = 'original')
mean = plt.plot(rolmean, color ="red", label ='Rolling Mean')
std = plt.plot(rolstd,color = 'green', label = 'rolling standard deviation')
plt.legend(loc ='best')
plt.title('Rolling mean and Standard deviation')
plt.show(block=False)

# Estimate trend
indexedDataset_logScale =np.log(indexedDataset)
plt.plot(indexedDataset_logScale)

movingAverage= indexedDataset_logScale.rolling(window =12).mean()
movingstd= indexedDataset_logScale.rolling(window=12).std()
plt.plot(indexedDataset_logScale)
plt.plot(movingAverage, color ='red')

datasetlogscaleminusmovingaverage = indexedDataset_logScale - movingAverage
datasetlogscaleminusmovingaverage.head(12)

datasetlogscaleminusmovingaverage.dropna(inplace=True)
datasetlogscaleminusmovingaverage.head(10)

from statsmodels.tsa.stattools import adfuller
def test_stationary(timeseries):

     #determine rolling stat
     movingAverage = timeseries.rolling(window=12).mean()
     movingstd = timeseries.rolling(window=12).std()


     orig = plt.plot(timeseries, color = 'blue', label ='original')
     mean = plt.plot(movingAverage, color = 'red', label='mean')
     std = plt.plot(movingstd, color ='green', label ='standard deviation')
     plt.legend(loc ='best')
     plt.title('Rolling Standard Deviation')
     plt.show(block = False)

     #perform Dickey-Fuller test:
     print('result of Dickey-Fuller Test:')
     dftest = adfuller(timeseries['volume'],autolag='AIC')
     dfoutput = pd.series(dftest[0:4], index = ['Test Statistics', 'p-Value', "#lag used", 'number of observations used'])
     for key, value in dftest[4].items():
         dfoutput['Critical Value (%s)'%key]= value
         print(dfoutput)




