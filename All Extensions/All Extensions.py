#	This script goes through all the files on the computer
#	looking for all the different extensions
#	it writes them in order of frequency to a text file
#	For more discoveries visit the author @ github.com/owbird/Discoveries

import os
import operator

# creating empty data sets
tot_files = {}

# checking for type of os
root_directory = "c:/" if os.name == "nt" else "/"

# looping through system
for root, _, files in os.walk(root_directory):

	# targeting files only
	for file in files:

		# taking extension
		ext = os.path.splitext(file)[1]

		# validating extension
		if ext == '':
		
			continue
			
		else:
		
			# adding the extension to a dictionary
			tot_files.setdefault(ext, 0)

		# going through the extensions in the dictionary
		if ext in tot_files.keys():

			# checking the extensions for match
			tot_files[ext] += 1	

# finding the total amount of extensions
sum_list = sum([_ for _ in tot_files.values()])

# creating a file
with open('Found Extensions.txt', 'w') as db:		

	# saving to file
	db.write(f'Total files: {sum_list}\n\n')	

	# going through extensions and thier values
	for key, value in sorted(tot_files.items(), key = operator.itemgetter(1), reverse = True):

		# finding the percentage
		per = round(float((value / sum_list) * 100),3)

		# saving to file
		txt = f'{key} => {value} => {per}%\n\n'
		
		db.write(txt)
