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
import random, string
def makePlate():
	#make a new plate, at time 13.37, temp 100 degrees, with 6 wells
	plate = Plate(13.37, 100.0, 6)
	#fill it with random numbers and print the desired output
	for i in range(6):
		plate.setWellValue(random.uniform(0,10), i)
	return plate

listofPlates = list()
for i in range(5):
	x = makePlate()
	listofPlates.append(x)


# x.printCSV()
# plate.printCSV()
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
		wellTemp = P.temp
		wellTime = P.time
		# Get the number of wells in the plate
		numWells = P.numWells
		# Print out the data as a single row of comma separated values
		# Initialize an empty string to build our string out of.
		stringValue = str(wellTemp) + ", " + str(wellTime) + ", " 

		#for every well in this plate
		for well in range(0, numWells):																										
		# Build the string by adding the data from this well to it.
			stringValue = stringValue + str(P.data[well]) + str(", ") 

		#the final constructed string	
		stringValue = stringValue[0:-2]

		return stringValue
		

def printPlates(Plates, csvFile):	
	if not isinstance(Plates, list) or not all(isinstance(p, Plate) for p in Plates):
		print "ERROR: Input is not a list of Plate objects!"
	else:
		with open(csvFile, "w") as WriteToCsvFile:
			# Write column headers
			WriteToCsvFile.write ("Temperature, Time, ")
			# Get first plate in series of Plates
			# Use its labels as column headers
			plate0 = Plates[0];
			WriteToCsvFile.write(", ".join(plate0.wellLabel)+"\n")
			
			# Write the data
			for plate in Plates:
				s = printPlate(plate)
				WriteToCsvFile.write (s+ "\n")
	

#---------------------------------------------------
# Now do it using your function (Dont touch this line of code either)
#printPlate(plate)
printPlates(listofPlates, 'test.csv')

