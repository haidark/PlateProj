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

import xml.etree.ElementTree as ET

tree = ET.parse('realData.xml')
#we need to prepend everything witht he namespace in order to search for it...
namespace = "{http://moleculardevices.com/microplateML}"
#Gets root from real data file
root = tree.getroot()

#def getWellXML(x, root):
	# This function gets the (x-1)-th well from the XML file.
#	if int(x) > 96:
#		print "Your input is incorrect"
#	else:
#		wave = root[1][0].find(namespace+'microplateData').find(namespace+'wave')
#		print wave[x-1][0].find(namespace+'rawData').text



def getWellXML(x, root):
	x = input("Please enter the file name: ")
	root = ET.fromstring()
	print root


#x = input("Please enter a number: ")
getWellXML(x, root)