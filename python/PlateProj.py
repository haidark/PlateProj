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

if len(sys.argv) != 3:
	print 'USAGE: '+sys.argv[0]+' <xml file> <csv file>'
	quit()

print "Reading the XML file..."
PlateList = readXMLFile(sys.argv[1])
print "Printing the CSV file..."
printPlates(PlateList, sys.argv[2])
print "Done!"