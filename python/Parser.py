###################################################
#Filename: Parser.py
#Author: Haidar Khan, Shuaib Peters
#Date: 3/24/15
###################################################
# Notes: (Anything after a '#' is a comment)
# This file contains the function which creates a list of Plate objects \
# from an xml file
###################################################

#Assignment for Shuaib Peters
from Plate import Plate
import xml.etree.ElementTree as ET

#we need to prepend everything witht he namespace in order to search for it...
namespace = "{http://moleculardevices.com/microplateML}"


a = raw_input("Please enter the file name: ")

def getWellXML(a):
	tree = ET.parse(a)
	root = tree.getroot()
	noOfWells = root[1][0][5].find(namespace+ 'noOfWells')
	print "The number of wells in your file is: ", noOfWells.text
	for child in root[1][0][5][3].iter(namespace+ 'rawData'):
		print child.tag
		print child.text
	

#getWellXML(a)

	temp = root[1][0][5][3].iter(namespace+ 'temperatureData')
	rawData = root[1][0][5][3].iter(namespace+ 'rawData')
	time = root[1][0][5][3].iter(namespace+ 'timeData')

	x = Plate(temp, time, 96)
	print x.getWellValue(numOfWells)

getWellXML(a)

#print type(-0.098)
