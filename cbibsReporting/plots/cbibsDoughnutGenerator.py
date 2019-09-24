# -*- coding: utf-8 -*-

from plots.cbibsDoughnutPlot import cbibsDoughnutPlot

class cbibsDoughnutGenerator():
    GOOD = "GOOD Value"
    NeNaU= "Not Evaluated, Not Available, Unknown"
    SUSPECT = "Questionable or Suspect"
    BAD = "BAD"
    MISSING = "MISSING"
      
      
    # Iterate over measurements and get the QC into an array
    def getGraphQcDataSet(self, measures):
        good=0
        notEval=0
        suspect=0
        bad=0
        missing=0
        unknown=0
        
        # Iterate
        for measure in measures:         
            if measure.qa == cbibsDoughnutGenerator.GOOD:
                good += 1
            elif measure.qa == cbibsDoughnutGenerator.NeNaU:
                notEval  +=1
            elif measure.qa == cbibsDoughnutGenerator.SUSPECT:
                suspect +=1
            elif measure.qa == cbibsDoughnutGenerator.BAD:
                bad +=1
            elif measure.qa == cbibsDoughnutGenerator.MISSING:
                missing+=1
            else:
                unknown += 1
                
        # Debugging message        
        if unknown >0:
            print('WARNING, found {} unknown QC'.format(unknown))
         
        # Create a dictionary with the counters    
        qcValues = {};    
        qcValues["Good"] = good;
        qcValues["Bad"] = bad;
        qcValues["Not Evaluated"] = notEval;
        qcValues["Suspect"] = suspect;
        if missing >0:
            qcValues["Missing"] = missing;
        if unknown >0:
            qcValues["Empty"] = unknown;
        
        return qcValues    
   
    def getDataToPlot(self, station, varActualName):
        return station.getDataToPlot(varActualName)
    

    def fillEmptyArray(self, emptyArray, measures):
        # fill the empty array
        for actualMess in measures:
            item = self.findItem(emptyArray, actualMess.time)
            if item != None:
                item.time = actualMess.time
                item.value = actualMess.value
                item.qa = actualMess.qa
    
    def findItem(self, emptyArray, time):
       
        for mess in emptyArray:
            # print("Looking for {} in {}".format(actualMess.time,mess.time))
            #print(mess.time, time)
            if mess.time == time:
                return mess
        return None
    
    
    def generateAPlot(self, shortName, longName, fullArray):
        cbibsDP = cbibsDoughnutPlot()

        # Get the data into a plotable array
        paramSet = self.getGraphQcDataSet(fullArray)
        varReportName = shortName + "-"+ longName
        varReportName +=  " ({} measures".format(len(fullArray))+")"
        myPlot = cbibsDP.makePlot(paramSet, varReportName)
        myPlot.show()
        
        
        
        
        