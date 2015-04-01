###################################################
#Filename: Printer.py
#Author: Haidar Khan, Azer Khan
#Date: 3/24/15
###################################################
# Notes: (Anything after a '#' is a comment)
# This file contains the function which prints a list of Plate objects \
# to a .csv file
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

#Assignment for Azer Khan
#Now I want you to write a function that takes as input a Plate object (P)
#It prints out the data in the Plate object in the manner discussed during\
#our first meeting. (Review your notes)
#---------------------------------------------------
#Here is the skeleton code for the function called 'printPlate'
def printPlate(P):
	#checking if it is an instance of the Plate class 
	if not (isinstance(P, Plate)):
		print "Sorry, not a valid input"
	else: 
		#You dont need to create a new plate, 
		#I passed one to you and you made sure it was a plate using the error checking code!!!


		# get the number of wells in the plate
		#You can use Bayah's accessor functions to get the number of wells, (totally unnecessary)
		numWells = P.getNumberOfWells()

		#or you can just get them using the '.' operator
		numWells = P.numWells


		# Print out the data as a single row of comma separated values
		# this works, but ...
		stringValue = str("") 
		#this is cleaner:
		stringVale = ""

		#perfect! this is a great for loop
		for well in range(0, numWells):
		 	stringValue = stringValue + str(p1.getWellValue(well)) + str(",")

		#removed indentation here so it doesnt print out all the substrings.
		print stringValue

	#You are done; to verify your results, make sure they match with the order \
	#That I printed out earlier in this file.


#---------------------------------------------------
# Now do it using your function (Dont touch this line of code either)
printPlate(plate)
