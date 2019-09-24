# -*- coding: utf-8 -*-
"""
Created on Tue Sep 17 12:07:15 2019

@author: Charles.Pellerin
"""

import datetime
import dateutil.parser

class CbibsMeasurement():
    """ Class to represent(object) a CBIBS Buoy """
    
    def __init__(self, time, value, qa):
        #print(type(time))
        # If this is created with a datetime don't parse it
        if (type(time) == datetime.datetime):
            self.time = time
        else:
            self.time = dateutil.parser.parse(time)
        
        # If this is not a value don't convert it
        if value != None:
            self.value = float(value)
        else:
            self.value = value
        
        self.qa = qa
       
    def __str__(self):
        output =  "    {}".format(self.time)
        output += ", {}".format(self.value)
        output += ", {}".format(self.qa)
        return output
    def __repr__(self):
        return self.__str__()

    def createFromJsonDictionary(jsonDictionary):
        cm = CbibsMeasurement(jsonDictionary['time'],jsonDictionary['value'],jsonDictionary['QA'])
        return cm
    
    def getTime(self):
        return self.time # dateutil.parser.parse(self.time)
    