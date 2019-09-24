# -*- coding: utf-8 -*-
"""
Created on Wed Sep 18 11:12:04 2019

@author: Charles.Pellerin
"""

import datetime
import pytz
from plots.cbibsDoughnutGenerator import cbibsDoughnutGenerator
from cbibsJson.vo.CbibsStationJsonMgr import CbibsStationJsonMgr


   
print("Starting to plot the QC\n")
# plt.close('all')

# Data set up for plotting
stationName='PL'
varActualName='sea_water_temperature'
# varActualName='battery_volts'
#varActualName='relative_humidit'
endDate = datetime.datetime.now( pytz.UTC)
startDate = endDate - datetime.timedelta(days=21)

# Get the data using the API
station = CbibsStationJsonMgr.getStationReadings(stationName, varActualName, startDate, endDate)
interval = station.getCbibsVariable(varActualName).interval

# print("--- Results\n")
# print(station)

# Now that I have the data, use the doughnut chart generator

doughPlotter = cbibsDoughnutGenerator()

# Get the measures from the station with this variable
measures = doughPlotter.getDataToPlot(station, varActualName)
if measures != None and len(measures) > 0:
    # Get the first measurement
    sampleTime = measures[0].getTime()
    emptyArray = CbibsStationJsonMgr.getEmptyTimeArray(sampleTime, int(interval), startDate, endDate)
    
    doughPlotter.fillEmptyArray(emptyArray, measures)
    doughPlotter.generateAPlot(station.shortName,station.getCbibsVariable(varActualName).reportName, emptyArray )
   
else:
    doughPlotter.generateAPlot()
    
    # paramSet = convertForGraphing(paramSet)


    