# -*- coding: utf-8 -*-
"""
Created on Tue Jul 16 14:31:51 2019

@author: Charles.Pellerin
"""

import matplotlib.pyplot as plt
import cbibsFileUtil
import cbibsPickleUtil
import operator

# Instructions
# Clean up the figures from the last run
# plt.close('all')

pickleDir ="pickles" # you will need to change this for your local path
parameter='sea_water_temperature'

# Get the name of the file you are looking for
stationFiles = cbibsFileUtil.getAllFiles(pickleDir, '.pkl')

all_qc = [0,0,0,0,0]
for stationFile in stationFiles:
    print("Found a file: " + stationFile)

    # Read the contents into memory, this may take up a lot of resources
    contents = cbibsPickleUtil.readPickleFile(stationFile)
    paramSet = cbibsPickleUtil.filterOnVariable(contents, parameter)
    qcGraph = cbibsPickleUtil.getGraphQcDataSet(paramSet)
    print(*qcGraph, sep = ", ")  
    all_qc = list(map(operator.add, all_qc, qcGraph))

# units = cbibsPickleUtil.getUnits(contents) # pull units for the chart
#dataShape = np.shape(contents)
#print("Pickle has {} rows".format(dataShape[0]))

# Filter and then sort the data
# paramSet = cbibsPickleUtil.sortData(paramSet)
# paramSet = convertForGraphing(paramSet)
print("Graph data ")
print(*all_qc, sep = ", ")  
'''
1	GOOD Value
4	BAD
2	Not Evaluated, Not Available, Unknown.
3	Questionable or Suspect.
9	MISSING
'''

# Pie chart, where the slices will be ordered and plotted counter-clockwise:
labels = 'GOOD Value','BAD', 'Not Evaluated', 'Questionable', 'MISSING'
sizes = all_qc
# explode = (0.1, 0, 0, 0,0)  # only "explode" the 2nd slice (i.e. 'Hogs')

fig1, ax1 = plt.subplots()
ax1.pie(sizes, labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=25)
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

plt.show()