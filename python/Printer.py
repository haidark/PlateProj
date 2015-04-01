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
	#TODO: Error checking on the input
	if not (isinstance(P, plate)):
		print "Sorry, not a valid input"
	else: 
		p1 = Plate(13.36, 100.0, 6)
		p1.data = (100,3)
		print 'Time  ', p1.time
		print 'Temp  ', p1.temp
		print p1.data

	#checking if it is an instance of the Plate class is sufficient

	#TODO: get the number of wells in the plate

	#TODO: Print out the data as a single row of comma separated values
	# Think of our plate (2x3) with 9 wells\
	# letters indexing rows and numbers indexing columns then;
	# Our data is in this order: A1, A2, A3, B1, B2, B3,
	# NOT ths order: A1, B1, A2, B2, A3, B3


	#You are done; to verify your results, make sure they match with the order \
	#That I printed out earlier in this file.



#---------------------------------------------------
# Now do it using your function (Dont touch this line of code either)
printPlate(plate)
