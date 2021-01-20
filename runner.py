import getopt, sys
from fetcher import fetch


argumentList = sys.argv[1:]
# Options
options = "heo:"

# Long options
long_options = ["Help", "Email", "Output ="]

try:
	# Parsing argument
	arguments, values = getopt.getopt(argumentList, options, long_options)
	
	# checking each argument
	for currentArgument, currentValue in arguments:

		if currentArgument in ("-h", "--Help"):
			print ("Diplaying Help")
			
		elif currentArgument in ("-e", "--Email"):
			# print ("Displaying file_name:", sys.argv[0])
			email = argumentList[1]
			fetch(email)
		elif currentArgument in ("-o", "--Output"):
			print ("Displaying file_name:", sys.argv[0])
except getopt.error as err:
	print (str(err))
