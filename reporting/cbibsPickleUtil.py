#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 15 15:43:43 2019

@author: cpellerin
"""

import pickle
import numpy as np


def readPickleFile(stationFile):
    with (open(stationFile, "rb")) as tmpFile:
        while True:
            try:
                return pickle.load(tmpFile)
            except EOFError:
                break


def filterOnVariable(pickleData, parameter):
    filtered = []
    for lineNum in range(np.shape(pickleData)[0]):
        line = pickleData[lineNum]
        #print(line)
        #var = input("Please enter something: ")
        if parameter == "all" or line[3] == parameter:
            # tmpdt = datetime.datetime(line[1])         
            filtered.append(line) 
    return filtered

''' Example Line in the pickle
('YS', datetime.datetime(2019, 5, 18, 0, 0, tzinfo=psycopg2.tz.FixedOffsetTimezone(offset=0, name=None)), 326.0, 'current_direction',
 'Currents', 9, 'Degrees Magnetic', 37.2006366666667, -76.26619, -2.5)
    0      1         2            3             4          5     6     7    8      9
station, obsDate, obsValue, parameterName, parameterGroup, QC, units, lat, lon, elevation
'''
# Read the entire pickle file and filter on the variable to graph
def getGraphDataSet(pickleData):
    filtered = []
    for lineNum in range(np.shape(pickleData)[0]):
        line = pickleData[lineNum]        
        # tmpdt = datetime.datetime(line[1])         
        filtered.append([line[1], line[2]])        
    return filtered

# Sort the data by date
def sortData(unsortedArray):
    # sortedArray = sorted(unsortedArray, key=lambda x: datetime.strptime(x[0], '%m/%d/%y %H:%M'), reverse=True)
    sortedArray = sorted(unsortedArray, key=lambda x: x[0], reverse=False)
    return sortedArray

def getUnits(contents):
    return contents[0][6]

def getFirstDate(contents):
    return contents[0][1]
