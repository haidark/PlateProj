###################################################
#Filename: Printer.py
#Author: Haidar Khan, Azer Khan
#Date: 3/24/15
###################################################
# Notes: (Anything after a '#' is a comment)
# This file contains the function which prints a list of Plate objects \
# to a .csv file
###################################################
from Plate import Plate

def printPlates(Plates, csvFile):
	if not isinstance(Plates, list) or not all(isinstance(p, Plate) for p in Plates):
		print ("ERROR: Input is not a list of Plate objects!")
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
				WriteToCsvFile.write (plate.printCSV()+ "\n")
#---------------------------------------------------
