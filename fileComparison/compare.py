# -*- coding: utf-8 -*-
"""
Created on Mon Feb 11 13:19:53 2019

@author: charles.pellerin
"""

# Import the regular expression library
import re

"""
Given a filename and a line of text search the file to find if it exists
"""
def findLineInFile(fileName, text):
    # Open file and read contents
    with open(fileName) as fp:  
        rLine = fp.readline()
        while rLine:
            # Strip white space
            rLine = rLine.strip()
            if rLine == text:
                # Found the line, exit with true
                return True
            # Get the next line
            rLine = fp.readline()
    return False    
    
# Optional, if running command line ask for the file names
# Ask the user to enter the names of files to compare
#fileName1 = input("Enter the first filename: ")
#fileName2 = input("Enter the second filename: ")

"""
Given two file names, iterate over the lines in the left file 
looking for the text in the right file
"""
def findInLeft(fileName1, fileName2):

    notInRight = list()
    with open(fileName1) as fp:  
       line = fp.readline()
       cnt = 1
       while line:
           aLine = line.strip()
           # Test if it is just doubles
           # regular expression to test for two double values separated by a comma
           # Skip lines that are just two doubles
           twoDoubleRegex='(([1-9][0-9]*\.?[0-9]*)|(\.[0-9]+))([Ee][+-]?[0-9]){,}(([1-9][0-9]*\.?[0-9]*)|(\.[0-9]+))([Ee][+-]?[0-9])'
           dubMatch = re.match(twoDoubleRegex, aLine, flags=0)
           if dubMatch:
               # print("Double match:::",aLine)
               # Skip lines that contain two doubles
               pass
           else:
               if not findLineInFile(fileName2,aLine):
                   notInRight.append(aLine)
           line = fp.readline()
           cnt += 1
    print(cnt,"Total lines in file:", fileName1)
    return notInRight


# Look for differences in these two files
fileName1='ENC007_10092018'
fileName2='ENC002_11232018'

print("Checking two config files")


# Print confirmation
print("-----------------------------------")
print("Comparing files ", " > " + fileName1, " < " +fileName2, sep='\n')
print("-----------------------------------")
notInRight = findInLeft(fileName1,fileName2);
for missing in notInRight:
    print("In ",fileName1," file but not in the ",fileName2,":",missing)
       

# Print confirmation
print("-----------------------------------")
print("Comparing files ", " > " + fileName2, " < " +fileName1, sep='\n')
print("-----------------------------------")
notInRight = findInLeft(fileName2,fileName1);
for missing in notInRight:
    print("In ",fileName2," file but not in the ",fileName1,":",missing)
    
    


