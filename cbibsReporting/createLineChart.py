# -*- coding: utf-8 -*-

# -*- coding: utf-8 -*-
"""
Created on Wed Sep 18 11:12:04 2019

@author: Charles.Pellerin
"""

import datetime
import pytz
from plots.cbibsLinePlotGenerator import cbibsLinePlotGenerator
from cbibsJson.vo.CbibsStationJsonMgr import CbibsStationJsonMgr


   
print("Starting a line plot\n")

# Option to close all of the open plots
# plt.close('all')

# Data set up for plotting
stationName='SR'
#varActualName='sea_water_temperature'
varActualName='battery_volts'
#varActualName='relative_humidity'
endDate = datetime.datetime.now( pytz.UTC)
startDate = endDate - datetime.timedelta(days=30)

# Get the data using the API
station = CbibsStationJsonMgr.getStationReadings(stationName, varActualName, startDate, endDate)
interval = station.getCbibsVariable(varActualName).interval
measures = station.getDataToPlot(varActualName)
print(measures)
# Got the data setup, now plot
plotTitle = station.shortName
units = station.getCbibsVariable(varActualName).units
reportName = station.getCbibsVariable(varActualName).reportName
linePlotter = cbibsLinePlotGenerator()
if measures != None and len(measures) > 0:
    sampleTime = measures[0].getTime()
    emptyArray = CbibsStationJsonMgr.getEmptyTimeArray(sampleTime, \
        int(interval), startDate, endDate)
    
    linePlotter.fillEmptyArray(emptyArray, measures)
    print("Original Data {}, filled data {}".format(len(measures),len(emptyArray)))
    plotData = linePlotter.getDataSet(emptyArray)
    plotTitle += "\n"+reportName + " plotted from \n{} to {}".format(startDate,endDate)
    plotTitle += "\n{}, values out of {}".format(len(measures),len(emptyArray))
    data = linePlotter.generatePlot(plotTitle, units, plotData)