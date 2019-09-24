#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 15 14:17:41 2019

@author: cpellerin
"""

import cbibsPickleUtil
import cbibsFileUtil
import numpy as np



# First, load up the pickle
pickleDir ="pickles" # you will need to change this for your local path
csvDir = "csv"
csvDateFormat="%Y-%m-%d %H:%M:%S"

# next specify the pickle you want to read, this is the file you created with pull_buoy_data.py
# remember that pickles load straight into memory, so leave enough room for that or yuo'll get paging
# Just specify the station, this will pick up the latest file for that station
stationName='YS'

# filter on a parameter or just pass all through
# parameter='sea_water_temperature'
parameter='all'


# Find a file in the pickle directory that begins with the station name
stationFile = cbibsFileUtil.getMostRecentStationFile(pickleDir, stationName, '.pkl')
print("Found a file: " + stationFile)

# Read the contents into memory, this may take up a lot of resources
contents = cbibsPickleUtil.readPickleFile(stationFile)

# Output the number of rows
dataShape = np.shape(contents)
print("Pickle has {} rows".format(dataShape[0]))

# Print out the first line just to see what's in the pickle
print(contents[0])

# Filter and then sort the data
paramSet = cbibsPickleUtil.filterOnVariable(contents, parameter)
paramSet = cbibsPickleUtil.sortData(paramSet)
print("CSV data has {} rows".format(len(paramSet)))


'''
Create CSV file from pickle data
         
('YS', datetime.datetime(2019, 5, 18, 0, 0, tzinfo=psycopg2.tz.FixedOffsetTimezone(offset=0, name=None)), 326.0, 'current_direction',
 'Currents', 9, 'Degrees Magnetic', 37.2006366666667, -76.26619, -2.5)

'''
startDT=cbibsPickleUtil.getFirstDate(contents)
outputPath = cbibsFileUtil.getFilePath(csvDir)
csvFile = cbibsFileUtil.createCbibsFile(stationName,csvDir, startDT,'.csv')

# now write the file
cbibsFileUtil.createCsvFile(csvFile, paramSet)
   