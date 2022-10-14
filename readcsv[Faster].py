import pandas as pd
import numpy as np
import math

filepath = 'worldcities.csv'

set1 = pd.read_csv(filepath, usecols=['lat', 'lng'])
set2 = pd.read_csv('worldcities.csv', usecols=['lat', 'lng'])
counter=[]

print('Enter the Distance from the site: ')
x = input()
x = int(x)

set2['lat'] = set2['lat'].mul(math.pi/180)
set2['lng'] = set2['lng'].mul(math.pi/180)

set2['sinlat'] = np.sin(set2['lat'])
set2['coslat'] = np.cos(set2['lat'])

for i in range(set1.shape[0]):
    c=0
    t=set2.copy(deep=False)
    lat1rs = math.sin(set1['lat'].values[i] * math.pi/180)
    lat1rc = math.cos(set1['lat'].values[i] * math.pi / 180)
    lng1r = set1['lng'].values[i] * math.pi/180

    t['dist'] = np.arccos((lat1rs * t['sinlat']) + (lat1rc * t['coslat'] * np.cos(t['lng']-lng1r))) * 6371000

    c = np.where(t['dist']<x, 1, 0)
    counter.insert(i, np.sum(c))

data = pd.read_csv(filepath, usecols=['lat', 'lng'])
data['count'] = counter
data.to_csv(filepath)