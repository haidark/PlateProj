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
#make a new plate, 5 rows, 6 columns at time 13.37 and temp 100 degrees
plate = Plate(5,6, 13.37, 100.0)
#fill it with random numbers and print the desired output
for i in range(5):
	for j in range(6):
		plate.setData(random.uniform(0,10), i,j)
		print plate.data[i][j]
#HK - END DO NOT MODIFY THIS CODE
#####################################################

#Assignment for Azer Khan
#Now I want you to write a function that takes as input a Plate object (P)
#It prints out the data in the Plate object in the manner discussed during\
#our first meeting. (Review your notes)
#---------------------------------------------------
#Here is the skeleton code for the function called 'printPlate'
def printPlate(P):
	print 'Delete this line of code; this function does nothing yet!'
	#TODO: Error checking on the input
	#checking if it is an instance of the Plate class is sufficient

	#TODO: get the dimensions of the plate

	#TODO: Print out the data matrix in ROW-MAJOR order (look this up)
	# Think of our plate (3x3) with \
	# letters indexing rows and numbers indexing columns then;
	# We want to print out in this order: A1, B1, C1, A2, B2, C2, A3, B3, C3.
	# NOT ths order: A1, A2, A3, B1, B2, B3, C1, C2, C3


	#You are done; to verify your results, make sure they match with the order \
	#That I printed out earlier in this file.




# Now do it using your function (Dont touch this line of code either)
printPlate(plate)
