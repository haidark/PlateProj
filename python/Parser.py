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
# Before we start coding, you need to learn more about the XML format for storing data
#I have made a simplified xml document that more or less resembles the form of the \
#data we will be working with. 
#TODO: Study this file carefully and try to draw a tree that resembles the structure \
#of the file similar to the trees I drew during our last meeting. (on paper)

#TODO: once you have an understanding of the structure of the XML tree, use the pyton XML parser \
#(documentation here: https://docs.python.org/2/library/xml.etree.elementtree.html) to read \
# the test.xml file into python.

#TODO: After you have done that, use the resulting tree to print the number of wells in the test.xml file.

#Imports the test file as an Element tree
#HKK: NO! this was correct before... This imports the parsing module that we will be using!

import xml.etree.ElementTree as ET

#HKK: This line is where test.xml is read as an element tree... but the filename is wrong here
tree = ET.parse('test.xml')

#Gets root from test file
root = tree.getroot()

# #Cool, now we have the root of the tree.
# # the root of the tree corresponds to the <microplate> tag in the file.
# #dont believe me? look at what this prints
# print root.tag
# #now we want to get the child of <microplate> that has the tag <noOfWells>
# #here is how we get a child by their tag name
# wellsElem = root.find('noOfWells')
# #that searches the children of root for the child with the tag 'noOfWells'
# #to prove I got it, ill print the tag and the text inside the tag
# print wellsElem.tag
# print wellsElem.text

# for rawData in root.iter('rawData'):
# 	print rawData.tag
# 	print rawData.text

# wave = root.find('wave')
# print wave[3].tag
# print wave[3].attrib
# print wave[3].find('oneDataSet').find('rawData').text





def getWellXML(x, root):

		if int(x) > 4:
			print "Your input is incorrect"
		else:
			wave = root.find('wave')
			print wave[x-1][0][0].text
			


x = input("Please enter a number from 1-4: ")
getWellXML(x, root)