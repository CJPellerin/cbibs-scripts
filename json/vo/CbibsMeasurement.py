# -*- coding: utf-8 -*-
"""
Created on Tue Sep 17 12:07:15 2019

@author: Charles.Pellerin
"""


class CbibsMeasurement():
    """ Class to represent(object) a CBIBS Buoy """
    
    def __init__(self, time, value, qa):
       self.time = time;
       self.value = value;
       self.qa = qa
       
    def __str__(self):
        output =  "    {}".format(self.time)
        output += ", {}".format(self.value)
        output += ", {}".format(self.qa)
        return output
       
    def createFromJsonDictionary(jsonDictionary):
        cm = CbibsMeasurement(jsonDictionary['time'],jsonDictionary['value'],jsonDictionary['QA'])
        return cm