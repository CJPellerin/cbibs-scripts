# -*- coding: utf-8 -*-
"""
Created on Wed Dec 28 09:04:47 2016
This is a python program that reads in the pickle files created in pull_buoy_data.py .
This function reads in an individual pickle and then plots the variables as a function of time.
@author: byron.kilbourne
"""


import numpy as np
import matplotlib.dates as mdates
import matplotlib.pyplot as plt
import cbibsPickleUtil
import cbibsFileUtil

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
# parameter='sea_water_temperature'
parameter='air_temperature'
dtQueryFormat="%Y-%m-%d %H:%M:%S"


# NOT USED
def convertForGraphing(data):
    converted = []
    for line in data:
        tmpDate = struct.unpack('<L', line[0])
        # datetime.datetime(line[0]) # .strftime(dtQueryFormat))
        converted.append([tmpDate,line[1]])
    return converted


    
# Get the name of the file you are looking for
stationFile = cbibsFileUtil.getMostRecentStationFile(pickleDir,station, '.pkl')
print("Found a file: " + stationFile)

# Read the contents into memory, this may take up a lot of resources
contents = cbibsPickleUtil.readPickleFile(stationFile)
units = cbibsPickleUtil.getUnits(contents) # pull units for the chart
dataShape = np.shape(contents)
print("Pickle has {} rows".format(dataShape[0]))

# Filter and then sort the data
paramSet = cbibsPickleUtil.filterOnVariable(contents, parameter)
paramSet = cbibsPickleUtil.getGraphDataSet(paramSet)
paramSet = cbibsPickleUtil.sortData(paramSet)
# paramSet = convertForGraphing(paramSet)
print("Graph data has {} rows".format(len(paramSet)))

# Create the 2D data to plot
x = []
y = []
for line in paramSet:
    # print("{},{}".format(line[0].strftime(dtQueryFormat),line[1]))
    x.append(line[0])
    y.append(line[1])
  

style.use('ggplot')

fig = plt.figure(parameter)
ax = plt.subplot()

# The b- makes a line graph
ax.plot_date(x,y,'bo-',markeredgecolor='b',markersize=2, linewidth=0.5)
# bo makes markers
# ax.plot_date(x,y,'b-',markeredgecolor='b',markersize=2, linewidth=0.5)


plt.title(parameter) # set the title of the graph
plt.xlabel('date') # the label is always date for the x-axis
plt.ylabel(units)
# myFmt = mdates.DateFormatter('%d')
ax.xaxis.set_major_formatter(mdates.DateFormatter('%m-%d %H:%M'))
for label in ax.xaxis.get_ticklabels():
    label.set_rotation(75)
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
