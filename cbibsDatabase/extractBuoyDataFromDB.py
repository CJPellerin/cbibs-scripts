# -*- coding: utf-8 -*-
"""
Created on Fri Dec 30 10:43:10 2016
This is a python program that reads data from the CBIBS PostgreSQL database and stores the results in a python pickle. Pickle is a funny name for a python binary data file, the information will be stored in such a way that it can be directly read back in to memory; magical. The stations and times to be pulled are defined at the beginning of the program. This python program requires python3.4 or later version due to dependence on the pathlib package.
718* the shack

@author: byron.kilbourne
"""

# Importations
import credentials
import pickle
from datetime import datetime
from psycopg2 import connect, sql, Error
from pathlib import Path # requires python 3.4 and up

import cbibsFileUtil

# Constants for running the script
dtQueryFormat="%Y-%m-%d %H:%M:%S"
startDTString = '2019-05-15 00:00:00'
stopDTString = '2019-06-15 00:00:00'
stations = ['YS','FL','SR','PL','GR','AN','J']
pickleDir ="pickles" # you will need to change this for your local path

def getConnString():
    host="host='"+credentials.host+"' "
    db="dbname='"+credentials.dbname+"' "
    port="port='"+credentials.port+"' "
    usr="user='"+credentials.username+"' "
    pswd="password='"+credentials.password+"' "
    return host+db+port+usr+pswd

def getQuery(station, startTime, stopTime):
    queryString = sql.SQL('select \
        sta.description, \
        fob.measure_ts, \
        fob.obs_value,  \
        dvar.actual_name, \
        dvar_grp.group_name, \
        qac.qa_code, \
        units.canonical_units, \
        fob.latitude, \
        fob.longitude, \
        fob.elevation \
        from cbibs.f_observation fob \
        inner join cbibs.d_station sta on sta.id = fob.d_station_id \
        inner join cbibs.d_variable dvar on dvar.id = fob.d_variable_id \
        inner join cbibs.d_qa_code_primary qac on qac.id = fob.d_qa_code_primary_id \
        left join cbibs.d_variable_group dvar_grp on dvar_grp.id = dvar.d_variable_group_id \
        left join cbibs.d_units units on units.id = dvar.d_units_id \
        where sta.description={} \
        and measure_ts >= {} \
        and measure_ts <= {} \
        order by fob.measure_ts desc').format(sql.Literal(station), \
        sql.Literal(startTime), \
        sql.Literal(stopTime))
    return queryString                  
                          

def debugSqlOutput(contents):
    count = 1
    for row in contents:
        print (row)
        count=count+1
        if count > 10:
            break

print("Starting to generate pickles")
try:
    # get a connect to the database
    conn = connect(getConnString())
    
    # create a data cursor() to hold the query output
    cur = conn.cursor()
    
    # create date time objects
    startDT=datetime.strptime(startDTString,dtQueryFormat)
    stopDT=datetime.strptime(stopDTString,dtQueryFormat)
    
    for stationName in stations:
        # Get a pickle file name
        pickleFile = cbibsFileUtil.createCbibsFile(stationName,pickleDir, startDT,'.pkl')
        if Path(pickleFile).is_file():
            continue
       
        '''
        The variable queryString is a user genereated SQL query which is modified 
        to take station and time limits from the loop function.   
        '''
        queryString = getQuery(stationName, startDT, stopDT)
        # Debug, print the whole query string
        print(queryString.as_string(conn))
       
        print('Querying ' + stationName + ' from ' + startDT.strftime(dtQueryFormat) \
              + ' to '+ stopDT.strftime(dtQueryFormat))
    
        # This executes the query
        cur.execute(queryString)
    
        # This dumps the query output in to contents
        contents = cur.fetchall()
        debugSqlOutput(contents)
        
        
        print('Writing ' + pickleFile)
        # This opens the pickle for writing
        with open(pickleFile,'wb') as output:
            # This dumps contents in to the pickle
            pickle.dump(contents,output,-1)
        
        del contents
except (Exception, Error) as error:
    print("Error fetching data from PostgreSQL table", error) 
finally:
    # closing database connection
    if (conn):
        cur.close()
        conn.close()
        print("PostgreSQL connection is closed \n")