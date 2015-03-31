###################################################
#Filename: Parser.py
#Author: Haidar Khan, Shuaib Peters
#Date: 3/24/15
###################################################
# Notes: (Anything after a '#' is a comment)
# This file contains the function which creates a list of Plate objects \
# from an xml file
###################################################
#HK - DO NOT MODIFY THIS CODE:
from Plate import Plate
import random
#make a new plate, at time 13.37, temp 100 degrees, with 30 wells
plate = Plate(13.37, 100.0, 6)
#fill it with random numbers and print the desired output
for i in range(6):
	plate.setData(random.uniform(0,10), i)
plate.printCSV()
#HK - END DO NOT MODIFY THIS CODE
#####################################################

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
import test as ET

<<<<<<< HEAD
tree = ET.parse('noOfWells_microplateData.xml')
=======
#HKK: This line is where test.xml is read as an element tree... but the filename is wrong here
tree = ET.parse('noOfWells_microvavePlateData.xml')

>>>>>>> origin/master
#Gets root from test file
root = tree.getroot()
