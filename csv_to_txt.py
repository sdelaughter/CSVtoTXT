#Convert a CSV file to an easily readable text file
#Go through each row and print each entry, preceeded by the column header

__version__ = "0.1"

import os
import sys
import csv
import time


def parse_csv(csv_file, output_file):
	"""Parse the CSV file to find contact and location information for freezers
	Parameters
	----------
	csv_file : string
		The full pathname of the CSV file containing contact information
		This path is set as the global variable CSV_PATH at the top of this file
	Returns
	-------
	entries: list
		A list of dictionaries, one for each row
		Each dictionary's keys are the column headers from the file's first row
	"""

	reader = csv.reader(open(csv_file, 'rU'))
	rows = []
	for row in reader:
		rows.append(row)
	header = rows.pop(0)

	#stdout=sys.stdout
	sys.stdout=open(output_file, 'w')
	for row in rows:
		for i in range(len(row)):
			print(header[i])
			print row[i]
			print('\n')
		print('--------------------------------')
		print('\n\n')
		

def main():
	"""Convert the input CSV file to an easily readable text file
	
	Parameters
	----------
	None
	
	Returns
	-------
	None
	
	"""
	
	input = sys.argv[1]
	path, filename = os.path.split(input)
	output_filename = str(filename.split('.')[0]) + '.txt'
	output = str(path) + '/' + str(output_filename)
	print(output)
	
	parse_csv(input, output)
	


if __name__ == '__main__':
	main()