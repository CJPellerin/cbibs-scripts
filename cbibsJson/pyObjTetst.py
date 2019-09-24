# -*- coding: utf-8 -*-
"""
Created on Tue Sep 17 10:52:16 2019

@author: Charles.Pellerin
"""

import datetime
import json

from vo.CbibsStationJsonMgr import CbibsStationJsonMgr


def load_data(file_name):
  with open(file_name, 'r') as file_data:
      return file_data.read()
  
def testReadingFile():  
    '''
       Test the method using a file
    '''
    fileName='rawJsonTest.txt'
    stationJson = load_data(fileName)
    print(stationJson)
    jsonDict = json.loads(stationJson)
    print("Here is a stations current reading\n")
    stationData = CbibsStationJsonMgr.createStationFromJson(jsonDict['stations'][0])
    print("--- Results\n")
    print(stationData)

def testGetCurrentReadings():
    '''
       Test the method to get the current readings
    '''
    print ("STARTING \n\n")
    stationName='FL'        
    print("Here is a stations current reading\n")
    stationData = CbibsStationJsonMgr.getCurrentReadings(stationName)
    print("--- Results\n")
    print(stationData)

def testGetStationReadings():
    '''
       Test the method to query the data
    '''
    print("Here are stations variable reading\n")
    stationName='FL'
    var='air_temperature'
    endDate = datetime.datetime.now()
    startDate = endDate - datetime.timedelta(days=3)
    station = CbibsStationJsonMgr.getStationReadings(stationName, var, startDate, endDate)
    print("--- Results\n")
    print(station)


testGetStationReadings()






