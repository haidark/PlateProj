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
#	-numRows - The number of rows on the plate (int > 0)
#	-numCols - The number of columns on the plate (int > 0)
#	-temp - The temperature the plate was at when recording took place (int/float)
#	-time - The time when the recording took place TODO: secs/mins? (int/float)
#	-data - a matrix of numRows rows and numCols columns containg well data
#		(list(list(float))) or numpy matrix?
#------------------------------------------------------------------
# The Plate class has the following methods:
#	-__init__ - constructor for Plate objects
#		arguments (args) - (numRows, numCols, temp, time)
#	-setData - sets an element ([row][col]) in the data matrix
#		args - (value, row, col)
#------------------------------------------------------------------
#Plate Class Declaration
class Plate:
	### DOCSTRING ###
	#Constructor
	def __init__(self, numRows, numCols, temp, time):
		#Error checking on input
		if not (isinstance(numRows, int) and isinstance(numCols, int)
			and	numRows > 0 and numCols > 0):
			print "Dimensions are invalid!"
		elif not (isinstance(temp, (float, int)) and isinstance(time, (float, int))):
			print "Invalid type for temp or time!"
		else:
			self.numRows = numRows
			self.numCols = numCols
			self.temp = temp
			self.time = time
			#initialize data to a matrix of zeros
			#Using list comprehensions (trust me this works)
			self.data = [[0 for x in range(numCols)] for y in range(numRows)]
	#sets the element in 'data' at the 'row'-th row and the 'col'-th column to 'value'
	def setData(self, value, row, col):
		#Error checking on input
		if row < 0 or row > self.numRows:
			print "Invalid row index!"
		elif col < 0 or col > self.numCols:
			print "Invalid column index!"
		elif not isinstance(value, (float, int)):
			print "Invalid type for value!"
		else:
		#Insert the value into data at the specified index
			self.data[row][col] = value
#------------------------------------------------------------------
#Testing code for Plate Class
#(only runs if running this file directly)
if __name__ == "__main__":
	p1 = Plate(2,3, 15, 2.2)
	p1.setData(100, 1,2)
	print 'Time: ', p1.time
	print 'Temp: ', p1. temp
	print p1.data

