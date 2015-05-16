###################################################
# Filename: Plate.py
# Authors: Haidar Khan, Shuaib Peters, Azer Khan
# Date: 3/24/15
###################################################
# Notes: (Anything after a '#' is a comment)
# This file unifies the 3 modules for the Plate Project
# 
###################################################

from Printer import printPlates
from Parser import readXMLFile
import sys

print "Reading the XML file."
PlateList = readXMLFile(sys.argv[1])
print "Printing the CSV file..."
printPlates(PlateList)
print "Done!"