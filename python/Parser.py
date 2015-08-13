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
	esChild = root.find(namespace+'experimentSection')

	PlatesDict = dict()

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
			# handle the #SAT special case
			splitRawRow = rawRow.split()
			# for i, x in enumerate(splitRawRow):
			# 	if x == '#SAT':
			# 		splitRawRow[i] = 'inf'

			rawRow = [float(x) if x != '#Sat' else float('inf') for x in splitRawRow ]
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
