# -*- coding: utf-8 -*-
"""
Created on Tue Jul 16 14:31:51 2019

@author: Charles.Pellerin
"""

import matplotlib.pyplot as plt
import cbibsFileUtil
import cbibsPickleUtil
import operator
#import numpy as np
# Instructions
# Clean up the figures from the last run
# plt.close('all')

pickleDir ="pickles" # you will need to change this for your local path
#parameter='sea_water_temperature'
#parameter='air_temperature'
# Get the name of the file you are looking for
stationFiles = cbibsFileUtil.getAllFiles(pickleDir, '.pkl')
def getParameterSummary(parameter):
    ''' This function takes a parameter name and puts the QC data into a 5-integer
    array
    '''
    all_qc = [0,0,0,0,0]
    for stationFile in stationFiles:
        print("Found a file: " + stationFile)
    
        # Read the contents into memory, this may take up a lot of resources
        contents = cbibsPickleUtil.readPickleFile(stationFile)
        paramSet = cbibsPickleUtil.filterOnVariable(contents, parameter)
        qcGraph = cbibsPickleUtil.getGraphQcDataSet(paramSet)
        print(*qcGraph, sep = ", ")  
        all_qc = list(map(operator.add, all_qc, qcGraph))
        return all_qc
    
    
waterTempSummary=getParameterSummary('sea_water_temperature')
airTempSummary=getParameterSummary('air_temperature')
windSpeedSummary=getParameterSummary('wind_speed')
seaWaterSalinitySummary=getParameterSummary('sea_water_salinity')
#currentAverageSpeedSummary=getParameterSummary('current_average_speed')


# units = cbibsPickleUtil.getUnits(contents) # pull units for the chart
#dataShape = np.shape(contents)
#print("Pickle has {} rows".format(dataShape[0]))

# Filter and then sort the data
# paramSet = cbibsPickleUtil.sortData(paramSet)
# paramSet = convertForGraphing(paramSet)
print("Graph data ")
#print(*all_qc, sep = ", ")  
'''
1	GOOD Value
4	BAD
2	Not Evaluated, Not Available, Unknown.
3	Questionable or Suspect.
9	MISSING
'''

#Pie chart, where the slices will be ordered and plotted counter-clockwise:
labels = 'GOOD','BAD', 'NOT EVALUATED', 'QUESTIONABLE', 'MISSING'
#sizes = all_qc
#Displays one pie chart for QC data corresponding to a specific parameter summary. To change the summary being plotted, alter line 69. 

fig1, ax1 = plt.subplots()
ax1.pie(waterTempSummary, autopct='%1.1f%%',
        shadow=False, startangle=90)
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
fig1 = plt.gcf()
fig1.set_size_inches(5,5)
circle = plt.Circle(xy=(0,0), radius=0.75, facecolor='white')
plt.gca().add_artist(circle)
ax1.set_title('Water Temperature')
plt.legend(labels, bbox_to_anchor=(1,0), loc="lower right", 
          bbox_transform=plt.gcf().transFigure)

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
plt.show()