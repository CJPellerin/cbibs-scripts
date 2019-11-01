# -*- coding: utf-8 -*-
"""
Created on Mon Sep 16 14:52:35 2019

@author: Charles.Pellerin
"""

# import jsonpickle

class CbibsStation():
    """ Class to represent(object) a CBIBS Buoy """
    
    def __init__(self, stationShortName='', stationLongName=''):
       # Station short name 'AN', 'YS', 'S', etc...
       self.shortName = stationShortName;
       
       # Station Long name 'Annapolis', 'York Spit', 'Susuehanna', etc...
       self.longName = stationLongName;
       
       # Any non-zero is false
       self.status = '';
       
       # A list of current parameters (CbibsParam array)
       # private $paramaterList = array ();
       
       # new values
       self.latitude = 0.0;
       self.longitude = 0.0;
       
       self.variableList = []
    
    def __str__(self):
        output = "Station ["+self.shortName + "]\n"
        output += "    Name: " + self.longName  + "\n"
        output += "    Active: {}".format(self.status) + "\n"
        output += "    lat/lon {},{}".format(self.latitude, self.longitude) + "\n"
        if len(self.variableList) == 0:
            output += "    No Variables"
        else:
            output += "    Variables:\n"
            for var in self.variableList:
                output += str(var)
        return output
    
    def addVariable(self, variable):
        self.variableList.append(variable)
    
    def getDataToPlot(self, varActualName):
        var = self.getCbibsVariable(varActualName)
        if var == None:
            return None
        return var.getMeasurements()
        
    def getCbibsVariable(self, varActualName):
        for var in self.variableList:
            if (var.actualName == varActualName):
                return var
        return None
        
    
    @staticmethod  
    def createFromJsonDictionary(jsonDictionary):
        # Convert the raw dictionary to a Cbibs Station Object
        station = CbibsStation(jsonDictionary['stationShortName'], jsonDictionary['stationLongName'])
        station.status = jsonDictionary['active']
        station.latitude = jsonDictionary['latitude']
        station.longitude = jsonDictionary['longitude']
        return station
        
    
    
    
    
    
    
    
    
    