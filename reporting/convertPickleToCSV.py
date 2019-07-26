#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 15 14:17:41 2019

@author: cpellerin
"""

import cbibsPickleUtil
import cbibsFileUtil
import numpy as np
from pathlib import Path


# First, load up the pickle
pickleDir ="pickles" # you will need to change this for your local path
csvDir = "csv"
csvDateFormat="%Y-%m-%d %H:%M:%S"

# next specify the pickle you want to read, this is the file you created with pull_buoy_data.py
# remember that pickles load straight into memory, so leave enough room for that or yuo'll get paging
# Just specify the station, this will pick up the latest file for that station
stationName='YS'
# parameter='sea_water_temperature'
parameter='all'



stationFile = cbibsFileUtil.getMostRecentStationFile(pickleDir, stationName, '.pkl')
print("Found a file: " + stationFile)

# Read the contents into memory, this may take up a lot of resources
contents = cbibsPickleUtil.readPickleFile(stationFile)

dataShape = np.shape(contents)
print("Pickle has {} rows".format(dataShape[0]))

print(contents[0][0])

# Filter and then sort the data
paramSet = cbibsPickleUtil.filterOnVariable(contents, parameter)
paramSet = cbibsPickleUtil.sortData(paramSet)
# paramSet = convertForGraphing(paramSet)
print("CSV data has {} rows".format(len(paramSet)))

'''
Create CSV file from pickle data
         
('YS', datetime.datetime(2019, 5, 18, 0, 0, tzinfo=psycopg2.tz.FixedOffsetTimezone(offset=0, name=None)), 326.0, 'current_direction',
 'Currents', 9, 'Degrees Magnetic', 37.2006366666667, -76.26619, -2.5)

'''
startDT=cbibsPickleUtil.getFirstDate(contents)
outputPath = cbibsFileUtil.getFilePath(csvDir)
csvFile = cbibsFileUtil.createCbibsFile(stationName,csvDir, startDT,'.csv')

# Check to see if the file exists, we want one csv per buoy
if Path(csvFile).is_file():
     print('This file exists, appending ... ')
     f = open(csvFile,"a")
else:
    print('creating new file ... ')
    f = open(csvFile,"w+")
        
        
for line in paramSet:
    # Uncomment if you want to see the output as it writes
    # print(line)
    outputLine = str(line[0]) +','+ str(line[1]) +','+ str(line[2]) +',' \
    + str(line[3]) +','+ str(line[4]) +','+ str(line[5]) + ',' + str(line[6]) +',' \
    + str(line[7]) +','+ str(line[8]) +','+ str(line[9]) + '\n'
    f.write(outputLine)    

f.close()
   