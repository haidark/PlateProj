###################################################
#Filename: Parser.py
#Author: Haidar Khan, Shuaib Peters
#Date: 3/24/15
###################################################
# Notes: (Anything after a '#' is a comment)
# This file contains the function which creates a list of Plate objects \
# from an xml file
###################################################

from Plate import Plate
import xml.etree.ElementTree as ET

#we need to prepend everything with the namespace in order to search for it
namespace = "{http://moleculardevices.com/microplateML}"
# reads a well formatted xml file
# input: xml file name
# output: dictionary - keys: csv file names, values: Lists of Plate objects
def readXMLFile(xmlFileName):
	tree = ET.parse(xmlFileName)
	root = tree.getroot()
	PlatesDict = dict()
	for esChild in root.findall(namespace+'experimentSection'):
		for psChild in esChild.findall(namespace+'plateSection'):
			plateSectionNameString = psChild.find(namespace+'plateSectionName').text
			#make sure string is a valid filename
			plateSectionFileName = ''.join(i for i in plateSectionNameString if i not in '\/:*?<>|')

			mpChild = psChild.find(namespace+'microplateData')
			PlatesDict[plateSectionFileName] = parseMicroPlateData(mpChild)

	return PlatesDict


# parses a microplateData tag in the xml file
# input: microplateData node
# output: a list of Plate objects
def parseMicroPlateData(mpChild):
		# retrieve number of wells
		noWells = mpChild.find(namespace+'noOfWells')
		numWells = int(noWells.text)

		# retrieve number of reads
		noReads = mpChild.find(namespace+'noOfReads')
		numReads = int(noReads.text)

		# retrieve temperature data
		temperatureData = mpChild.find(namespace+'temperatureData')
		tempData = [float(x) for x in temperatureData.text.split()]

		# Get into wave element
		wave = mpChild.find(namespace+'wave')

		# Store all data in two matrices
		rawData = dict()
		timeData = list()
		labels = dict()
		wells = wave.findall(namespace+'well')
		for well in wells:
			# get the well label
			label = well.get('wellName')
			# get the well index
			wellIndex = int(well.get('wellID'))-1

			#extract data from well element
			oneDataSet = well.find(namespace+'oneDataSet')
			rawRow = oneDataSet.find(namespace+'rawData').text
			
			# handle the #SAT special case
			splitRawRow = rawRow.split()
			rawRow = [float(x) if x != '#Sat' else float('inf') for x in splitRawRow ]
			
			for r in range(len(rawRow), numReads):
				rawRow.append(0.0)

			# extract time from well element
			timeDataTag = oneDataSet.find(namespace+'timeData')
			if timeDataTag is not None:
				timeRow = [float(x) for x in timeDataTag.text.split()]
			else:
				timeRow = [-1 for i in range(numReads)]
			
			labels[wellIndex] = label
			rawData[wellIndex] = rawRow

		timeData = timeRow

		# create list of plate objects
		Plates = list()
		for r in range(numReads):
			p = Plate(tempData[r], timeData[r], numWells)
			for wellIndex, rawRow in rawData.items():
				p.setWellValue(rawRow[r], wellIndex, labels[wellIndex])
			Plates.append(p)
		return Plates
