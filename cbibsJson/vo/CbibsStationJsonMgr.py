# -*- coding: utf-8 -*-
"""
Created on Tue Sep 17 13:01:56 2019

@author: Charles.Pellerin
"""

import urllib
import requests
import datetime
import pytz

from cbibsJson.vo.CbibsStation import CbibsStation
from cbibsJson.vo.CbibsVariable import CbibsVariable
from cbibsJson.vo.CbibsMeasurement import CbibsMeasurement
import matplotlib.dates as mdates
class CbibsStationJsonMgr():
    
    @staticmethod
    def createStationFromJson(stationJson):
        station = CbibsStation.createFromJsonDictionary(stationJson)
  
        # get the measurement
        varList = stationJson['variable']
        for var in varList:
            cvar = CbibsVariable.createFromJsonDictionary(var)
            # print (cvar)
            measures = var['measurements']
            for m in measures:
                cm = CbibsMeasurement.createFromJsonDictionary(m)
                cvar.addMeasurement(cm)
            station.addVariable(cvar)
        return station
    
    # Read the json into a string
    # cbibsStationJson = load_data("rawJsonTest.txt")
    # Convert to a dictionary
    @staticmethod
    def getCurrentReadings(stationName):
        r = requests.get('https://mw.buoybay.noaa.gov/api/v1/json/station/'+stationName+'?key=7ec7ab1844a142a5f14e9b7fc261cd2c30c70f8b')
        jsonic = r.json()
        # Get the first station for testing
        stationJson = jsonic['stations'][0];
        # print(stationJson)
        station = CbibsStationJsonMgr.createStationFromJson(stationJson)
        return station
    
    @staticmethod
    def getStationReadings(stationName, var, startDate, endDate):
        protocol = "https://"
        url = "mw.buoybay.noaa.gov"
        port = "443"
        path = "/api/v1/json/query/"
        uri = protocol+url+":"+port+path
        uri += stationName 
        
        # Create the GET params
        sdString = startDate.strftime('%Y-%m-%dT%H:%M') +"+00"
        edString = endDate.strftime('%Y-%m-%dT%H:%M') +"+00"
        getParams = {}
        getParams['var'] = var
        getParams['sd'] = sdString
        getParams['ed'] = edString
        getParams['key'] = '7ec7ab1844a142a5f14e9b7fc261cd2c30c70f8b'
         
        print(uri)
        urie = urllib.parse.urlencode(getParams)
        print(urie)
        r = requests.get(uri + "?" + urie)
        jsonic = r.json()
        # print (jsonic)
        # Get the first station for testing
        stationJson = jsonic['stations'][0];
        
        # print(stationJson)
        station = CbibsStationJsonMgr.createStationFromJson(stationJson)
        return station
    
    @staticmethod
    def getEmptyTimeArray(sampleMeasurement, interval, startDate, endDate):
        
        # Take the sample, and subtract the interval until you get to the bounds
        # The first time is going to be the sample date      
        newStartTime = CbibsStationJsonMgr.getStartDate(sampleMeasurement, startDate, interval)
        
        emptyArray = [];
        # This is now the starting date
        
        endDate = endDate.replace(tzinfo=pytz.utc)
        # Move the start time forward one
        while newStartTime < endDate:          
            tempMess =  CbibsMeasurement(newStartTime, None, None)          
            emptyArray.append(tempMess)
            newStartTime = newStartTime + datetime.timedelta(minutes=(interval/60))
        
        print("StartDate {}, EndDate {}, interval {} ".format(startDate, endDate, interval))
        return emptyArray
 
    
    @staticmethod
    def getEmptyTimeArrayRange(sampleMeasurement, interval, startDate, endDate):
        """ Use the mat lab dates function instead of a loop to make the array
        Use this to test the speed difference"""
        newStartTime = CbibsStationJsonMgr.getStartDate(sampleMeasurement, startDate, interval)
        endDate = endDate.replace(tzinfo=pytz.utc)
        
        # Generate a series of dates (these are in matplotlib's internal date format)
        emptyArray = mdates.drange(newStartTime,endDate, datetime.timedelta(minutes=(interval/60)))    
        return emptyArray
    
    
    @staticmethod
    def getStartDate(sampleMeasurement, startDate, interval):
        newStartTime = sampleMeasurement.replace(tzinfo=pytz.utc)
        while newStartTime > startDate:    
          #tempMeasure = tempMeasure - datetime.timedelta(seconds=interval)
          newStartTime = newStartTime - datetime.timedelta(minutes=(interval/60))
          
        
        # the start time has crossed the border, move forward one
        newStartTime = newStartTime + datetime.timedelta(minutes=(interval/60))
        print("Empty array start time {}".format(newStartTime ))
        return newStartTime  
        
        
        
        
        
        
        
        