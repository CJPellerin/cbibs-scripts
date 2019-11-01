# -*- coding: utf-8 -*-
"""
Created on Thu Aug  1 12:41:58 2019

@author: Charles.Pellerin
"""

class PiePlotData:
    
    
    
    def __init__(self, qcName, count):
        self.qcName = qcName
        self.count = count
  
    def getLbl(self, total):
        pct = self.count/total * 100
        return self.qcName + " {:.1f}%".format(pct)
     
    