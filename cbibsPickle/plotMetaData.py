# -*- coding: utf-8 -*-
"""
Created on Thu Aug  1 13:07:05 2019

@author: Charles.Pellerin
"""
import piePlotData

class PlotMetaData:
    
    
    
    
    def __init__(self, paramName, paramLegend):
        self.paramName = paramName
        self.paramLegend = paramLegend
        self.totalPlotPoints = 0
        self.plotDataList = []
    
    def addQcList(self,qcArray):
        self.totalPlotPoints = sum(qcArray)
        ppd = piePlotData.PiePlotData("Good",qcArray[0])
        self.plotDataList.append(ppd)
        bad = piePlotData.PiePlotData("Bad",qcArray[1])
        self.plotDataList.append(bad)
        notEval = piePlotData.PiePlotData("Not Eval",qcArray[2])
        self.plotDataList.append(notEval)
        suspect = piePlotData.PiePlotData("Suspect",qcArray[3])
        self.plotDataList.append(suspect)
        missing = piePlotData.PiePlotData("Missing",qcArray[4])
        self.plotDataList.append(missing)
        
    def getDataList(self):
        lbls = []
        for dataPt in self.plotDataList:
            if dataPt.count != 0:
                lbls.append(dataPt.count)
        return lbls
    
    def getLabelList(self):
        lbls = []
        for dataPt in self.plotDataList:
            if dataPt.count != 0:
                lbls.append(dataPt.getLbl(self.totalPlotPoints))
        return lbls