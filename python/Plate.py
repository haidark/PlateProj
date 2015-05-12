###################################################
#Filename: Plate.py
#Author: Haidar Khan
#Date: 3/24/15
###################################################
# Notes: (Anything after a '#' is a comment)
# This file contains the class declaration for the Plate class \
# in addition to some test code
###################################################

# The Plate class models a 96-well microplate (or any other plates) at \
# a specific time and temperature
#------------------------------------------------------------------
# The Plate class has the following attributes:
#	-numWells - The number of wells on the plate (int > 0)
#	-temp - The temperature the plate was at when recording took place (int/float)
#	-time - The time when the recording took place TODO: secs/mins? (int/float)
#	-data - an array of numWells elements containg well data (list(float))
#	-wellLabel - a list of strings, same size as data (list(string))	
#------------------------------------------------------------------
# The Plate class has the following methods:
#	-__init__ - constructor for Plate objects
#		arguments (args) - (temp, time, numWells)
#	-setData - sets an element ([well]) in the data array
#		args - (value, well)
#	-printCSV - prints the data
#------------------------------------------------------------------
#Plate Class Declaration
class Plate:
	### DOCSTRING ###
	#Constructor
	def __init__(self, temp, time, numWells):
		#Error checking on inputs
		if not (isinstance(numWells, int) and numWells > 0):
			print "Invalid number of wells!"
		elif not (isinstance(temp, (float, int)) and isinstance(time, (float, int))):
			print "Invalid type for temp or time!"
		else:
			self.numWells = numWells
			self.temp = temp
			self.time = time
			#initialize data to an array of zeros
			#Using a list comprehension (trust me this works)
			self.data = [0 for x in range(numWells)]
			#initialize wellLabels to strings of 0-numWells
			self.wellLabel = [str(x) for x in range(numWells)]
	
	#sets the 'well'-th element in 'data' to 'value'
	def setWellValue(self, value, well, label):
		#Error checking on input
		if well < 0 or well >= self.numWells:
			print "Invalid well index!"
		elif not isinstance(value, (float, int)):
			print "Invalid type for value!"
		elif not isinstance(label, str):
			print "Invalid type for label!"
		else:
		#Insert the value into data at the specified index
			self.data[well] = value
			self.wellLabel[well] = label
	
	def getWellValue(self, well):
		#Error checking on input
		if well < 0 or well >= self.numWells:
			print "Invalid well index!"
		else:
			return self.data[well]

	def printCSV(self):
		print ", ".join([str(x) for x in self.data])	
#------------------------------------------------------------------
#Testing code for Plate Class
#(only runs if running this file directly)
if __name__ == "__main__":
	p1 = Plate(15, 2.2, 6)
	p1.setWellValue(100, 3)
	print 'Time: ', p1.time
	print 'Temp: ', p1. temp
	print p1.data

