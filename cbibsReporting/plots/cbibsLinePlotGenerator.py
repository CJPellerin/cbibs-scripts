# -*- coding: utf-8 -*-

from plots.cbibsLinePlot import cbibsLinePlot
import numpy as np
import pylab

class cbibsLinePlotGenerator():
    
    def findItem(self, emptyArray, time):
       
        for mess in emptyArray:
            # print("Looking for {} in {}".format(actualMess.time,mess.time))
            #print(mess.time, time)
            if mess.time == time:
                return mess
        return None
    
    def fillEmptyArray(self, emptyArray, measures):
        # fill the empty array
        for actualMess in measures:
            item = self.findItem(emptyArray, actualMess.time)
            if item != None:
                item.time = actualMess.time
                item.value = actualMess.value
                item.qa = actualMess.qa
    
    def interpolate_gaps(self, values, limit=None):
        """
        Fill gaps using linear interpolation, optionally only fill gaps up to a
        size of `limit`.
        """
        values = np.asarray(values)
        i = np.arange(values.size)
        # print(values)
        # valid = np.isfinite(values)
        valid = np.isfinite(values)
        filled = np.interp(i, i[valid], values[valid])
    
        if limit is not None:
            invalid = ~valid
            for n in range(1, limit+1):
                invalid[:-n] &= invalid[n:]
            filled[invalid] = np.nan
    
        return filled
      
    # Iterate over measurements
    def getDataSet(self, measures):
        plotData = {}
        for measure in measures:
            # Only add measures with values
            #if hasattr(measure, 'value'):
            plotData[measure.getTime()]=measure.value
            #elif
                
        
        return plotData
    
    def generatePlot(self, plotTitle, units, plotData):
        clp = cbibsLinePlot()
        print(type(plotData))
        
        # Sort the data and handle the None values
        sortedDateKeys = sorted(plotData.keys()) #, key=plotData.get)
        sortedValues=[]
        for dateKey in sortedDateKeys:
            if plotData[dateKey] != None:
                sortedValues.append(plotData[dateKey])
                #print(type(plotData[dateKey]))
            else:
                #print("Addind a NAN")
                sortedValues.append(pylab.nan)
        #sortedValues = self.interpolate_gaps(sortedValues)
        
       
        clp.generatePlot(plotTitle, units, sortedDateKeys, sortedValues)