#! /usr/bin/env python
#coding=utf-8
#Analyze Coco Cola's Stock
#Author: Billy Li (junchenl@andrew.cmu.edu)

import csv
import numpy as np
import math
import matplotlib.pyplot as plt
from datetime import datetime as dt
from collections import defaultdict as dict
from collections import Counter
import matplotlib.dates as mdates
import warnings
warnings.filterwarnings("ignore") #The polyfit function will give lots of annoying warnings!
#task 1

print 'Loading data...'
start_time =  dt.now()
dateConverter = lambda d : dt.strptime(d,'%Y/%m/%d %H:%M:%S')

data = np.genfromtxt('./table_cce.csv',
                     delimiter=',',names=True,dtype=(type(dt),float,float,float,float,float,float),converters={1: dateConverter})
end_time = dt.now()
print 'It took your computer', end_time-start_time,'to load the data.'
type = type(data)
print 'The data type stored in memory is',type
rows = data.shape[0]
print 'There are', rows, 'rows.'
columns = len(data[0,])
print 'Three are', columns, 'columns.'
print '>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>'
print data[2][:]
time_today = []
open_today = []
for i in range(0, len(data)):
        time_today.append(data[i][0])
        open_today.append(data[i][2])
        i += 1
plt.scatter(time_today, open_today, color ='blue', alpha = 1.00)
plt.xlabel('Time')
plt.ylabel('Open Price')
plt.title('Open Price VS Time',loc='left')
plt.grid(True)
plt.show()
