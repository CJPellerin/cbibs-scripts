# -*- coding: utf-8 -*-
"""
Created on Tue May 21 8:35 AM 2019

@author: byron.kilbourne
"""
import numpy as np
import pickle
#import psycopg2
from pathlib import Path

#years = ['2007','2008','2009','2010','2011','2012','2013','2014','2015','2016']
#stations = ['RC','J','N','YS','FL','SR','PL','UP','GR','AN','SN','S']
#stations = ['J','N','YS','FL','SR','PL','UP','GR','AN','SN','S']
#years = ['2007','2008','2009','2010','2011','2012','2013','2014','2015','2016','2017','2018']
stations = ['J','YS','FL','SR','PL','GR','AN']
#stations = ['SR']
years = ['2019']
pkl_date = 'Jun_19'
for sta in stations:
    for year in years:
        yp1 = str(int(year)+1)
        t0 = '\''+year+'-01-01 00:00:00\''
        t1 ='\''+yp1+'-01-01 00:00:00\''

        inputPath = 'C:\\Users\\byron.kilbourne\\CBIBS\\pfiles\\pickles\\'
        inputName = sta+'_'+pkl_date+'.pkl'
        inputString = inputPath+inputName
        # Check to see if the file exists, skip missing pickles
        if Path(inputString).is_file():
            print('loading pickle ... ')
            
        else:
            print('pickle not found, moving on ... ')
            continue
        # Open pickles to get data
        with open(inputString,'rb') as input:
            contents = pickle.load(input)

        outputPath = 'C:\\Users\\byron.kilbourne\\CBIBS\\data\\pkltocsv\\'
        outputName = sta+'_'+pkl_date+'_data.csv'
        outputString = outputPath+outputName
        # Check to see if the file exists, we want one csv per buoy
        if Path(outputString).is_file():
            print('This file exists, appending ... ')
            f = open(outputString,"a")
        else:
            print('creating new file ... ')
            f = open(outputString,"w+")
        
        a = np.shape(contents)
        year = np.zeros(a[0],dtype=np.int16)
        month = np.zeros(a[0],dtype=np.int16)
        day = np.zeros(a[0],dtype=np.int16)
        hour = np.zeros(a[0],dtype=np.int16)
        minute = np.zeros(a[0],dtype=np.int16)
        second = np.zeros(a[0],dtype=np.int16)
        
        measID = np.zeros(a[0],dtype=np.int16)
        meas = np.zeros(a[0])
        measName = []
        
        qcflag = np.zeros(a[0],dtype=np.int8)
        elev = np.zeros(a[0],dtype=np.float)
        
        stationID = np.zeros(1,dtype=np.int8)
        stationName = []
        
        mTime = np.zeros(a[0])
        sTime = []
        dTime = []
        
        i=0
        while i < a[0]:
        #while i < 1000:
        #while i < 1:
            line = contents[i]
            if i == 0:
                #print(line)       
                stationID = line[4]
                stationName.append(line[5])
            
            meas[i] = line[1]
            measID[i] = line[2]
            if measID[i]!=2:
                continue
            qcflag[i] = line[6]
            elev[i] = line[9]
#            measName.append(line[3])    
            b = line[0]
            year[i] = b.year
            month[i] = b.month
            day[i] = b.day
            hour[i] = b.hour
            minute[i] = b.minute
            #b = dt.datetime(year[i],month[i],day[i],hour[i],minute[i],second[i])        
#            dTime.append(b)
#            mTime[i] = mdates.date2num(b)
#            sTime.append(b.strftime('%Y%m%dT%H:%M:%S.%f'))
            
            outputLine = str(stationID) +','+ str(measID[i]) +','+ str(meas[i]) +','+ str(year[i]) +','+ str(month[i]) +','+ str(day[i]) +','+ str(hour[i]) +','+ str(minute[i]) +','+ str(second[i]) +','+str(qcflag[i])+','+str(elev[i])+'\n'
            f.write(outputLine)
            i += 1
        f.close()