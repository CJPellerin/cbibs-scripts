#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 15 16:01:02 2019

@author: cpellerin
"""

import os
import glob
from pathlib import Path


dtFileFormat="%Y_%m_%d_%H_%m"

# Get the directory containing pickle files
def getFilePath(fileDir):
    # Here i've used the date of the meeting to makr the files, there is a better way.
    if not os.path.exists(fileDir):
        print("Directory " + fileDir + " does not exist, exiting")
        # Optional, create the dir if not found?
        os.makedirs(fileDir)
    outputString = fileDir + os.sep
    return outputString

# Get the newest pickle file that starts with the name of the station
def getMostRecentStationFile(fileDir, station, suffux):
    pickleLocalDir = getFilePath(fileDir)
    allPickles = pickleLocalDir + station + '_*' + suffux
    stationPickle = max(glob.glob(allPickles),key=os.path.getctime )
    return stationPickle    

# Get the newest pickle file that starts with the name of the station
def getAllFiles(fileDir, suffux):
    pickleLocalDir = getFilePath(fileDir)
    allPickles = pickleLocalDir + '*_*' + suffux
    stationPickle = glob.glob(allPickles)
    return stationPickle   

# get the name of a file, create the directory if it doesn't exist
def createCbibsFile(stationName, pickleDir,  startDT, suffux):
    # Here i've used the date of the meeting to makr the files, there is a better way.
    outputName = stationName + '_' + startDT.strftime(dtFileFormat) + suffux
    if not os.path.exists(pickleDir):
        print("Directory " + pickleDir + " does not exist, creating")
        os.makedirs(pickleDir)
    outputString = pickleDir + os.sep + outputName
    return outputString


def createCsvFile(csvFile, paramSet):
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
