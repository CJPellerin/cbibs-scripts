# -*- coding: utf-8 -*-

import matplotlib.pyplot as pyplot


class cbibsDoughnutPlot():
    
    #def __init__(self):
       # self.labels = 'GOOD','BAD', 'NOT EVALUATED', 'QUESTIONABLE', 'MISSING'
         
    def createColorMap(self, paramSet):
        colorMap = []
        for val in paramSet.keys():
            if val == "Good":
                colorMap.append("green")
            elif val == "Bad":
                colorMap.append("red")
            elif val == "Not Evaluated":
                colorMap.append("orange")
            elif val == "Suspect":
                colorMap.append("yellow")
            elif val == "Missing":
                colorMap.append("cyan")
            elif val == "Empty":
                colorMap.append("gray")
        return colorMap     
        
    def makePlot(self, paramSet, varReportName):
        colorMap = self.createColorMap(paramSet)
        fig1, ax1 = pyplot.subplots()
        ax1.pie(paramSet.values(), colors=colorMap, autopct='%1.1f%%', shadow=False, startangle=90)
        ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
        fig1 = pyplot.gcf()
        
        # plot size
        fig1.set_size_inches(5,5)
        
        # Create as an open circle
        circle = pyplot.Circle(xy=(0,0), radius=0.75, facecolor='white')
        pyplot.gca().add_artist(circle)
        ax1.set_title(varReportName)
        
        # Configure the legend
        pyplot.legend(paramSet.keys(), bbox_to_anchor=(1,0), \
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
    
