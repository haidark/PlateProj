###################################################
# Filename: Plate.py
# Authors: Haidar Khan, Shuaib Peters, Azer Khan
# Date: 3/24/15
###################################################
# Notes: (Anything after a '#' is a comment)
# This file unifies the 3 modules for the Plate Project
#
###################################################

from Printer import printPlates
from Parser import readXMLFile
import sys, os.path

files = list()
if len(sys.argv) < 2:
	print( '(-) USAGE: '+sys.argv[0]+' <xml file>')
	print ('(-) This program takes a properly formatted xml file and transforms the data into a csv file.')
	files.append(input('Enter the filename (with path) of your xml file: '))
else:
	files = sys.argv[1:]

for xmlFile in files:
	if not os.path.isfile(xmlFile):
		print ('(--) ERROR: '+xmlFile+' does not exist.')
		continue

	fileName = os.path.splitext(xmlFile)[0]

	print ("(+) Reading "+xmlFile+'...')
	PlatesDict = readXMLFile(xmlFile)
	print ('(+) Generating .csv files...')
	printPlates(PlatesDict)
print ("(++) Finished!")

from tkinter import tix as tk


class Application(tk.Frame):
	def __init__(self, master=None):
		tk.Frame.__init__(self, master)
		self.pack()
		self.createWidgets()

	def createWidgets(self):
		self.hi_there = tk.Button(self)
		self.hi_there["text"] = "Hello World\n(click me)"
		self.hi_there["command"] = self.say_hi
		self.hi_there.pack(side="right")

		self.fileEntry = tk.FileEntry(self)
		self.fileEntry.pack(side="left", fill='x')

		self.QUIT = tk.Button(self, text="QUIT", fg="red", command=root.destroy)
		self.QUIT.pack(side="bottom")

	def say_hi(self):
		print(self.fileEntry.config())



root = tk.Tk()
app = Application(master=root)
app.mainloop()
