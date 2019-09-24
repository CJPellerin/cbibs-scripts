# -*- coding: utf-8 -*-


class cbibsDonutVo(object):
    ''' This class represents an item in the donutChart. 
    It has a count, name, and can generate a label'''
    
    def __init__(self, count, name):
        self.count = count
        self.name = name
        
        
        
    def getLabel(self, sums):
        percent = 100.*self.count/sums        
        label = '{0} - {1:1.1f}%'.format(self.name, percent)
        return label
        
    def __str__(self):
        output = "VO ["+self.name + "]"
        output += "    Count: {}".format(self.count)# + "\n"
        return output

    def __repr__(self):
        return self.__str__()   
    def __cmp__(self, other):
        print("Compare")
        print(type(self.count))
        if hasattr(other, 'count'):
            return self.count.__cmp__(other.count)