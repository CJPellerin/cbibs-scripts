# -*- coding: utf-8 -*-
"""
Created on Tue Feb  5 12:34:00 2019

@author: byron.kilbourne
"""

# -*- coding: utf-8 -*-
"""
Created on Wed Dec 28 09:04:47 2016
This is a python program that reads in the pickle files created in pull_buoy_data.py .
This function reads in an individual pickle and then plots the variables as a function of time.
@author: byron.kilbourne
"""
# Importations
import os
import glob

import numpy as np
import datetime
import matplotlib.dates as mdates
import matplotlib.pyplot as plt
import pickle
#import matplotlib.ticker as mticker # this is a fancier way of displaying dates
from matplotlib import style
import struct

# Instructions
# Clean up the figures from the last run
plt.close('all')

# First, load up the pickle
pickleDir ="pickles" # you will need to change this for your local path

# next specify the pickle you want to read, this is the file you created with pull_buoy_data.py
# remember that pickles load straight into memory, so leave enough room for that or yuo'll get paging
# Just specify the station, this will pick up the latest file for that station
station='YS'
parameter='sea_water_temperature'
dtQueryFormat="%Y-%m-%d %H:%M:%S"


# Get the directory containing pickle files
def getPicklePath():
    # Here i've used the date of the meeting to makr the files, there is a better way.
    if not os.path.exists(pickleDir):
        print("Directory " + pickleDir + " does not exist, exiting")
        exit()
    outputString = pickleDir + os.sep
    return outputString

def getPickleFile(station):
    pickleLocalDir = getPicklePath()
    allPickles = pickleLocalDir + station + '_*.pkl'
    stationPickle = min(glob.glob(allPickles),key=os.path.getctime )
    return stationPickle    

def readPickleFile(stationFile):    
    with (open(stationFile, "rb")) as tmpFile:
        while True:
            try:
                return pickle.load(tmpFile)
            except EOFError:
                break


''' Example Line
('YS', datetime.datetime(2019, 5, 18, 0, 0, tzinfo=psycopg2.tz.FixedOffsetTimezone(offset=0, name=None)), 326.0, 'current_direction',
 'Currents', 9, 'Degrees Magnetic', 37.2006366666667, -76.26619, -2.5)
'''
def filterOnVariable(pickleData, parameter):
    filtered = []
    for lineNum in range(np.shape(pickleData)[0]):
        line = pickleData[lineNum]
        #print(line)
        #var = input("Please enter something: ")
        if (line[3] == parameter):
            # tmpdt = datetime.datetime(line[1])         
            filtered.append([line[1], line[2]])        
    return filtered


def sortData(unsortedArray):
    # sortedArray = sorted(unsortedArray, key=lambda x: datetime.strptime(x[0], '%m/%d/%y %H:%M'), reverse=True)
    sortedArray = sorted(unsortedArray, key=lambda x: x[0], reverse=False)
    return sortedArray

def convertForGraphing(data):
    converted = []
    for line in data:
        tmpDate = struct.unpack('<L', line[0])
        # datetime.datetime(line[0]) # .strftime(dtQueryFormat))
        converted.append([tmpDate,line[1]])
    return converted

    
# Get the name of the file you are looking for
stationFile = getPickleFile(station)
print("Found a file: " + stationFile)

# Read the contents into memory, this may take up a lot of resources
contents = readPickleFile(stationFile)
dataShape = np.shape(contents)
print("Pickle has {} rows", dataShape[0])

paramSet = filterOnVariable(contents, parameter)
paramSet = sortData(paramSet)
# paramSet = convertForGraphing(paramSet)

print("Pickle has rows", len(paramSet))
x = []
y = []
for line in paramSet:
    print("{},{}".format(line[0].strftime(dtQueryFormat),line[1]))
    x.append(line[0])
    y.append(line[1])


style.use('ggplot')

fig = plt.figure(parameter)
ax = plt.subplot()

# plot the data by day of the year, a little easier than screwing with datetimes
# plot the date in a date referenced frame
# dates = mdates.date2num(paramSet[0])
ax.plot_date(x,y,'bo',markeredgecolor='b',markersize=2)
#ax.plot_date(mTime[ind[good]],tdat[good],'bo',markeredgecolor='b')
#ax.plot_date(mTime[ind[bad]],tdat[bad],'ro',markeredgecolor='r')
#ax.plot_date(mTime[ind[suspect]],tdat[suspect],'go',markeredgecolor='g')
plt.title(parameter)
plt.xlabel('date')
myFmt = mdates.DateFormatter('%d')

# plt.gcf().autofmt_xdate()
#ax.xaxis.set_major_formatter(mdates.DateFormatter('%m-%d'))
for label in ax.xaxis.get_ticklabels():
    label.set_rotation(90)
#plt.subplots_adjust(left=0.09, bottom=0.20, right=0.94, top=0.90, wspace=0.2, hspace=0)
plt.show()
    

'''
These are all the variable types in postgreSQL database

air_pressure
air_temperature
mass_concentration_of_chlorophyll_in_sea_water
mass_concentration_of_oxygen_in_sea_water
current_average_speed
current_average_direction
grid_latitude
grid_longitude
relative_humidity
sea_surface_wave_mean_height
sea_surface_wave_from_direction
sea_surface_maximum_wave_height
sea_surface_wave_significant_height
sea_surface_wind_wave_period
sea_water_acidity
sea_water_salinity
sea_water_temperature
simple_turbidity
wave_direction_spread
wind_from_direction
wind_speed
wind_speed_of_gust
seanettle_prob
heat_index
wind_chill
sea_water_freezing_point
ph_volts
sea_water_specific_electrical_conductivity
alternate_chlorophyll_units
instrument_depth
current_speed
current_direction
battery_volts
battery_volts_ysi
percent_oxygen_saturation
sea_water_temperature_aux_1
solar_panel_charge_current
water_depth
'''    

'''
    I tried to color by flag type, it was working, then it stopped, not sure why
    good = np.where(qcflag == 1)
    bad = np.where(qcflag[ind] == 4)
    suspect = np.where(qcflag[ind] == 3)
    '''
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
'''
