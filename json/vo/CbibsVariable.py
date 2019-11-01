# -*- coding: utf-8 -*-
"""
Created on Tue Sep 17 11:23:20 2019

@author: Charles.Pellerin
"""


# import jsonpickle

class CbibsVariable():
    """ Class to represent(object) a CBIBS Buoy """  
    def __init__(self, reportName, actualName, interval, units, group, elevation):
       self.reportName = reportName;
       self.actualName = actualName;
       self.interval = interval;
       self.units = units;
       self.group = group;
       self.elevation = elevation;
       self.measurements = []
       
    def __str__(self):
        output =  "   Variable ("+self.actualName + ", "+ self.reportName + ")\n"
        output += "    interval: {}".format(self.interval)  + "\n"
        output += "    units: " + self.units + "\n"
        output += "    group: " + self.group + "\n"
        output += "    elevation: {}".format(self.elevation) + "\n"
        if len(self.measurements) == 0:
            output += "    No Measurements\n"
        else:
            output += "    Measurements:\n"
            for mess in self.measurements:
                output += str(mess) +"\n"
        return output

    def addMeasurement(self, measure):
        self.measurements.append(measure)

     
    def createFromJsonDictionary(jsonDictionary):
         rname = jsonDictionary['reportName']
         aname = jsonDictionary['actualName']
         i = jsonDictionary['interval']
         u = jsonDictionary['units']
         g = jsonDictionary['group']
         e = jsonDictionary['elevation']
         cvar = CbibsVariable(rname, aname, i, u, g, e)
         return cvar