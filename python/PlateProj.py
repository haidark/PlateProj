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
import sys, os.path

if len(sys.argv) < 2:
	print '(-) USAGE: '+sys.argv[0]+' <xml file>'
	print '(-) This program takes a properly formatted xml file and transforms the data into a csv file.'
	quit()

for xmlFile in sys.argv[1:]:
	if not os.path.isfile(xmlFile):
		print '(--) ERROR: '+xmlFile+' does not exist.'
		continue

	fileName = os.path.splitext(xmlFile)[0]

	print "(+) Reading "+xmlFile+'...'
	PlateList = readXMLFile(xmlFile)
	print "(+) Printing to "+fileName+'.csv...'
	printPlates(PlateList, fileName+'.csv')
print "(++) Finished!"