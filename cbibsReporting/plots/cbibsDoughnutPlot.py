# -*- coding: utf-8 -*-

import matplotlib.pyplot as pyplot
import numpy as np

from plots.cbibsDonutVo import cbibsDonutVo

class cbibsDoughnutPlot():
    
    #def __init__(self):
       # self.labels = 'GOOD','BAD', 'NOT EVALUATED', 'QUESTIONABLE', 'MISSING'
       
    def createLabelForLegend(self, paramSet, colorMap, x, y):
       
        
        porcent = 100.*y/y.sum()        
        labels = ['{0} - {1:1.1f}%'.format(i,j) for i,j in zip(x, porcent)]
        
        #colorMap, labels, dummy =  zip(*sorted(zip(colorMap, labels, y),
         #                                 key=lambda x: x[2],
          #                                reverse=True))
         
        return labels
    
    # Use the type to get a color for the graph
    def makePlot(self, parent, paramSet, varReportName):
        mapVos = [];
        totalCount = 0
        for name in paramSet.keys():
            print (name)
            vo = cbibsDonutVo(paramSet[name],name)
            totalCount+= paramSet[name]
            print(vo)
            mapVos.append(vo)
        
        # Sort the objects based on key        
        mapVos.sort(key=lambda x: x.count, reverse=True)
        print(mapVos)
        
        x = []
        y = []
        labels = []
        colorMap = []
        # Now I have a sorted list, create the graphing data
        for mapVo in mapVos:
             labels.append(mapVo.getLabel(totalCount))
             x.append(mapVo.count)
             y.append(mapVo.name)
             # Use custom colors for the text based labels
             colorMap.append(parent.getGraphColor(mapVo.name))
    
        fig1, ax1 = pyplot.subplots()


        # startangle is where to start the values, 90 is the top
        # autopct='%1.1f%%', will make automatic percentages, but they overlap
        ax1.pie(x, colors=colorMap,  labeldistance=1.45, \
                shadow=False, startangle=90)
        # ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
        fig1 = pyplot.gcf() 
       
        
        # plot size
        fig1.set_size_inches(5,5)
        
        # Create as an open circle
        circle = pyplot.Circle(xy=(0,0), radius=0.75, facecolor='white')
        pyplot.gca().add_artist(circle)
        ax1.set_title(varReportName)
        
        # Configure the legend
        pyplot.legend(labels, bbox_to_anchor=(1,0), \
            loc="lower right", bbox_transform=pyplot.gcf().transFigure)
        
        #Displays multiple pie charts on one figure
        '''
        fig1, axs = plt.subplots(2, 2, figsize=(7, 7))
        #This is the water temperature pie chart
        axs[0, 0].pie(waterTempSummary, autopct='%1.f%%', pctdistance=1.4, labeldistance=1.2,
                shadow=False, startangle=25)
        #This axs is the air temperature pie chart
        axs[1, 0].pie(airTempSummary, autopct='%1.1f%%', pctdistance=1.4, labeldistance=1.2,
                shadow=False, startangle=25)
        #This is the wind speed pie chart
        axs[0, 1].pie(windSpeedSummary, autopct='%1.1f%%', pctdistance=1.3, labeldistance=1.2,
                shadow=False, startangle=25)
        #This is the salinity pie chart
        axs[1, 1].pie(seaWaterSalinitySummary, autopct='%1.1f%%', pctdistance=1.4, labeldistance=1.2,
                shadow=False, startangle=25)
        
        fig1.suptitle('Monthly QC Data: All Stations', fontsize=16)
        axs[0,0].set_title('Water Temperature')
        axs[1,0].set_title('Air Temperature')
        axs[0,1].set_title('Wind Speed')
        axs[1,1].set_title('Sea Water Salinity')
        plt.legend(labels, bbox_to_anchor=(1,0), loc="lower right", 
                                  bbox_transform=plt.gcf().transFigure)
        #plt.pie(labels=labels, autopct='%1.0f%%', pctdistance=1.1, labeldistance=1.2)
        '''
        return pyplot# plt.show()
    
