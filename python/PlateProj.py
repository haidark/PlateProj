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

if len(sys.argv) >= 2:	# if we have command line args, dont run the GUI
	files = sys.argv[1:]

	for xmlFile in files:
		if not os.path.isfile(xmlFile):
			print ('(--) ERROR: '+xmlFile+' does not exist.')
			continue

		fileName = os.path.splitext(xmlFile)[0]

		print ("(+) Reading "+xmlFile+'...')
		PlatesDict = readXMLFile(xmlFile)
		print ('(+) Generating .csv file(s)...')
		printPlates(PlatesDict)
	print ("(++) Finished!")

else:	#otherwise run the GUI
	from tkinter import *
	from tkinter.ttk import *
	from tkinter.filedialog import askopenfilename, askdirectory
	# define GUI class
	class Application(Frame):
		def __init__(self, master=None):
			Frame.__init__(self, master)
			self.pack(expand=1, fill='both')
			self.createWidgets()
			self.fileName = None
			self.outDir = '.'

		def createWidgets(self):

			self.inLabel = Label(self)
			self.inLabel['text'] = "Choose an input XML file."
			self.inLabel.pack()

			self.browse = Button(self)
			self.browse["text"] = "Browse"
			self.browse["command"] = self.openFileDialog
			self.browse.pack()

			self.outLabel = Label(self)
			self.outLabel['text'] = "(Optional) Select an output folder."
			self.outLabel.pack()

			self.outputDir = Button(self)
			self.outputDir['text'] = 'Select Folder'
			self.outputDir['command'] = self.selectOutputDir
			self.outputDir.pack()

			self.genLabel = Label(self)
			self.genLabel['text'] = "Generate CSV file(s)."
			self.genLabel.pack()

			self.generate = Button(self)
			self.generate["text"] = "Generate"
			self.generate["command"] = self.generateCSV
			self.generate.pack()

			self.Quit = Button(self, text="Exit", command=root.destroy)
			self.Quit.pack()

		def openFileDialog(self):
			name = askopenfilename()
			if name:
				self.fileName = name
				print("(+) File Selected: "+self.fileName)

		def selectOutputDir(self):
			name = askdirectory()
			if name:
				self.outDir = name
				print("(+) Folder Selected: "+self.outDir)

		def generateCSV(self):
			if self.fileName:
				xmlFile = self.fileName
				print ("(+) Reading "+xmlFile+'...')
				PlatesDict = readXMLFile(xmlFile)
				print ('(+) Generating .csv file(s)...')
				printPlates(PlatesDict, self.outDir)
				print ("(++) Finished!")
			else:
				print("(-) ERROR: No File Selected")

	# run the GUI
	root = Tk()
	root.style = Style()
	root.style.theme_use('winnative')
	app = Application(root)
	app.master.title("Plate Project")
	app.mainloop()

	# print( '(-) USAGE: '+sys.argv[0]+' <xml file>')
	# print ('(-) This program takes a properly formatted xml file and transforms the data into a csv file.')
	# files.append(input('Enter the filename (with path) of your xml file: '))
