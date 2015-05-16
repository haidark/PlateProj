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


#a = raw_input("Please enter the file name: ")

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

#getWellXML(a)

#print type(-0.098)

def readXMLFile(xmlFileName):
	tree = ET.parse(xmlFileName)
	root = tree.getroot()
	child = root.find(namespace+'experimentSection')
	child = child.find(namespace+'plateSection')
	child = child.find(namespace+'microplateData')
	
	# retrieve number of wells 
	noWells = child.find(namespace+'noOfWells')
	numWells = int(noWells.text)

	# retrieve number of reads
	noReads = child.find(namespace+'noOfReads')
	numReads = int(noReads.text)
	
	# retrieve temperature data
	temperatureData = child.find(namespace+'temperatureData')
	tempData = [float(x) for x in temperatureData.text.split()]
	
	# Get into wave element
	wave = child.find(namespace+'wave')
	
	# Store all data in two matrices
	rawData = list(list())
	timeData = list()
	labels = list()
	for w in range(numWells):
		# get the w-th well
		well = wave[w]
		# get the well labels
		labels.append(well.get('wellName'))

		#extract data from well element
		well = well.find(namespace+'oneDataSet')
		rawRow = well.find(namespace+'rawData').text
		rawRow = [float(x) for x in rawRow.split()]
		for r in range(len(rawRow), numReads):
			rawRow.append(0.0)

		# extract time from well element
		timeRow = well.find(namespace+'timeData').text
		timeRow = [float(x) for x in timeRow.split()]

		rawData.append(rawRow)
	
	timeData = timeRow
	# create list of plate objects
	Plates = list()
	for r in range(numReads):
		p = Plate(tempData[r], timeData[r], numWells)
		for w in range(numWells):
			p.setWellValue(rawData[w][r], w, labels[w])
		Plates.append(p)
		
	return Plates


readXMLFile('realData.xml')