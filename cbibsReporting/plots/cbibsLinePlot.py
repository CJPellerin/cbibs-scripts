# -*- coding: utf-8 -*-

import matplotlib.pyplot as pyplot
import matplotlib
import matplotlib.dates as mdates

class cbibsLinePlot():
    
    def generatePlot(self, plotTitle, units, sortedDateKeys, sortedValues):
        matplotlib.style.use('ggplot')
        
        fig = pyplot.figure(plotTitle)
        ax = pyplot.subplot()
        
        # The b- makes a line graph
        ax.plot_date(sortedDateKeys, sortedValues,'bo-',markeredgecolor='b',markersize=2, linewidth=0.5)
        # bo makes markers
        # ax.plot_date(x,y,'b-',markeredgecolor='b',markersize=2, linewidth=0.5)
        
        
        pyplot.title(plotTitle) # set the title of the graph
        pyplot.xlabel('date') # the label is always date for the x-axis
        pyplot.ylabel(units)
        # myFmt = mdates.DateFormatter('%d')
        ax.xaxis.set_major_formatter(mdates.DateFormatter('%m-%d %H:%M'))
        for label in ax.xaxis.get_ticklabels():
            label.set_rotation(75)
        #plt.subplots_adjust(left=0.09, bottom=0.20, right=0.94, top=0.90, wspace=0.2, hspace=0)
        pyplot.show()
    