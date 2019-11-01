# -*- coding: utf-8 -*-
"""
Created on Tue Feb  5 12:34:00 2019

@author: byron.kilbourne
"""

# -*- coding: utf-8 -*-
"""
Created on Wed Dec 28 09:04:47 2016
This is a python program that reads in the pickle files created in pull_buoy_data.py . This function reads in an individual pickle and then plots the variables as a function of time.
@author: byron.kilbourne
"""
# Importations
import numpy as np
import datetime as dt
import matplotlib.dates as mdates
import matplotlib.pyplot as plt
import pickle
#import matplotlib.ticker as mticker # this is a fancier way of displaying dates
from matplotlib import style

# Instructions
# Clean up the figures from the last run
plt.close('all')

# First, load up the pickle
# you will need to specify the path to the files *> note the weird slashes
fpath = 'C:\\Users\\byron.kilbourne\\CBIBS\\pfiles\\pickles\\'
# next specify the pickle you want to read, this is the file you created with pull_buoy_data.py
# remember that pickles load straight into memory, so leave enough room for that or yuo'll get paging
#fname = 'SR_2016to2017.pkl'
fname = 'PL_May_20.pkl'

with open(fpath+fname,'rb') as input:
    contents = pickle.load(input)

# Then, do stuff to the data
# Start by unpacking the database output

# initialize all the arrays
a = np.shape(contents)
year = np.zeros(a[0],dtype=np.int16)
month = np.zeros(a[0],dtype=np.int16)
day = np.zeros(a[0],dtype=np.int16)
hour = np.zeros(a[0],dtype=np.int16)
minute = np.zeros(a[0],dtype=np.int16)
second = np.zeros(a[0],dtype=np.int16)

measID = np.zeros(a[0],dtype=np.int16)
meas = np.zeros(a[0])
measName = []

qcflag = np.zeros(a[0],dtype=np.int8)

stationID = np.zeros(1,dtype=np.int8)
stationName = []

mTime = np.zeros(a[0])
sTime = []
dTime = []

# read the contents in to arrays
i=0
while i < a[0]:
#while i < 1:
    line = contents[i]
    if i == 0:
        #print(line)       
        stationID = line[4]
        stationName.append(line[5])
    
    meas[i] = line[1]
    measID[i] = line[2]
    qcflag[i] = line[6]
    measName.append(line[3])    
    b = line[0]
    year[i] = b.year
    month[i] = b.month
    day[i] = b.day
    hour[i] = b.hour
    minute[i] = b.minute
    #b = dt.datetime(year[i],month[i],day[i],hour[i],minute[i],second[i])        
    dTime.append(b)
    mTime[i] = mdates.date2num(b)
    sTime.append(b.strftime('%Y%m%dT%H:%M:%S.%f'))

    i += 1

# I print out the last line just to see if it is working, you don't have to do this    
print(str(year[-1]) +' '+ str(month[-1]) +' '+ str(day[-1]) +' '+ \
      str(hour[-1]) +' '+ str(minute[-1]) +' '+ str(second[-1]))
print(mdates.num2date(mTime[-1]))
print(sTime[-1])

'''
These are all the variable types in postgreSQL database

1: air_pressure
2: air_temperature
3: mass_concentration_of_chlorophyll_in_sea_water
4: mass_concentration_of_oxygen_in_sea_water
5: current_average_speed
7: current_average_direction
9: grid_latitude
10: grid_longitude
11: relative_humidity
13: sea_surface_wave_mean_height
15: sea_surface_wave_from_direction
16: sea_surface_maximum_wave_height
17: sea_surface_wave_significant_height
18: sea_surface_wind_wave_period
19: sea_water_acidity
21: sea_water_salinity
24: sea_water_temperature
25: simple_turbidity
28: wave_direction_spread
29: wind_from_direction
30: wind_speed
31: wind_speed_of_gust
34: seanettle_prob
35: heat_index
36: wind_chill
37: sea_water_freezing_point
38: ph_volts
39: sea_water_specific_electrical_conductivity
40: alternate_chlorophyll_units
49: instrument_depth
50: current_speed
51: current_direction
74: battery_volts
75: battery_volts_ysi
77: percent_oxygen_saturation
78: sea_water_temperature_aux_1
80: solar_panel_charge_current
85: water_depth
92: remove_me
'''
# initialize an array of unique variable names
unName = []
# get an array of unique measurement types by ID
unID, unInd = np.unique(measID,return_index=True)
# populate array of unique names
for n in range(0,len(unID)):
    unName.append(measName[unInd[n]])

# set plot style, be creative!
style.use('ggplot')
    
# you'll need this if you want to plot by yearday
refyear = dTime[1].year
refdate = mdates.date2num(dt.datetime(refyear,1,1,0,0,0))

# prints a list of measurement IDs with actual names to the output
# uncomment if you want to see the names
#for n in range(0,len(unID)):
#    print(str(unID[n])+': '+unName[n])

for n in range(0,len(unID)):
    # this is list of measurement IDs to skip plotting
    if unID[n] in [5,6,7,13,14,20,31,34,35,36,37,38,42,43,45,50,51,75,85,92]:
        continue
    
    ind = np.where(measID==unID[n])
    tdat = meas[ind]
    ''' 
    I tried to color by flag type, it was working, then it stopped, not sure why
    good = np.where(qcflag == 1)
    bad = np.where(qcflag[ind] == 4)
    suspect = np.where(qcflag[ind] == 3)
    '''
    fig = plt.figure(unName[n])
    ax = plt.subplot()
    # plot the data by day of the year, a little easier than screwing with datetimes
    #plt.plot_date(mTime[ind]-refdate,meas[ind],'bo',markeredgecolor='b')
    # plot the date in a date referenced frame
    ax.plot_date(mTime[ind],meas[ind],'bo',markeredgecolor='b')
    #ax.plot_date(mTime[ind[good]],tdat[good],'bo',markeredgecolor='b')
    #ax.plot_date(mTime[ind[bad]],tdat[bad],'ro',markeredgecolor='r')
    #ax.plot_date(mTime[ind[suspect]],tdat[suspect],'go',markeredgecolor='g')
    plt.title(str(unID[n]) +': '+ unName[n])
    plt.xlabel(str(refyear)+ ' yearday')
    #xticks(rotation='vertical')
    #ax.xaxis.set_major_formatter(mdates.DateFormatter('%m-%d'))
    for label in ax.xaxis.get_ticklabels():
        label.set_rotation(90)
    plt.subplots_adjust(left=0.09, bottom=0.20, right=0.94, top=0.90, wspace=0.2, hspace=0)
    plt.show()
    