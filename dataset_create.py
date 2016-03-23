from __future__ import print_function
import sys
import os
from os import listdir
from os.path import isfile, join
import glob


directory = sys.argv[1]
work_dir = sys.argv[2]
family = directory
samples = r"."+"/"+work_dir+"/"+directory+"/mist/"+"*.mist"
global k
k = 1000000000000000000000000000000000000

global increment

increment = 0

def line_count(fname):
	global non_blank_count
	non_blank_count = 0
	with open(fname) as infp:
    		for line in infp:
       			if line.strip():
          			non_blank_count += 1
	return non_blank_count

def mist_2_time(fname):
	increment = 0
        count_list = []
	file_out = open("./"+work_dir+"/"+directory+"/dat/"+id+"-"+family+".dat", "a")
	line_numbers = line_count(fname)
	print(fname)
	with open(fname) as file:
                for line in file:
			increment = increment + 1 
                        bad_words = ['#']
                        if not any(bad_word in line for bad_word in bad_words):
                                line_split = line.split('|')
                                lineok = line_split[0]
                                lineok = str(lineok)
                                output = len(lineok.split())
                                count_list.append(output)
				print(line_numbers)
				if increment  <= k:
                        		print(output, file = file_out)
					if increment == (line_numbers-1):
						print(output, file = file_out)
						print("0", file = file_out)
						break
				elif increment > k:
					print("0", file = file_out)
					increment
					break
					
		count_list = count_list[:k]
		count_list.append(0)
	return count_list[:k]
		#print(count_list[:k], file = file_out)
			



for path in glob.glob(samples):
	dirname, filename = os.path.split(path)
        filename_split = filename.split('-')
	id = filename_split[0]
	time_series = mist_2_time("./"+work_dir+"/"+directory+"/mist/"+filename)
	#file_out = open("./"+directory+"/dat/"+id+"-"+family+".dat", "a")
	#print(time_series, file = file_out)
	#NEWCOMMENT15GENNAIOfinal_out = open("./final/dataset.dat", "a")
	#NEWCOMMENTprint(id+","+str(time_series)+","+str(family), file = final_out)
	



	
