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

def readXMLFile(xmlFileName):

	#we need to prepend everything with the namespace in order to search for it
	namespace = "{http://moleculardevices.com/microplateML}"

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
