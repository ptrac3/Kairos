import sys
import time
import os
import glob
import itertools
from dtw import dtw
from itertools import combinations
from itertools import permutations
from itertools import combinations_with_replacement

first_run = None

directory = sys.argv[1]

samples = r"."+"/"+directory+"/training/"+"*.dat"

filenames = []

time_list = []


count = 0

first_run = None

minimum = None

maximum = None

prototype = None

prototype_max = None
distance_dict = {}

somma = None



for path in glob.glob(samples):
        dirname, filename = os.path.split(path)
        filename_split = filename.split('-')
        
	sample_family = filename_split[1]
	id = filename_split[0]
        sample_load = [int(x) for x in open("./"+directory+"/training/"+filename).readlines()]
	filenames.append(filename)
	time_list.append(sample_load)
time_combinations = list(combinations(time_list, 2))
file_combinations = list(combinations(filenames, 2))


for round in range(0, len(file_combinations)):
	
	filenameA = str(file_combinations[count][0])
        filenameB = str(file_combinations[count][1])
	
	#if filenameA == filenameB:
		#print "Files are the same, not calculating distance"
		#count = count + 1		
	dist, cost, path = dtw(time_combinations[count][0], time_combinations[count][1])	
	
	distance_dict.setdefault(filenameA, []).append(dist)
	distance_dict.setdefault(filenameB, []).append(dist)
	print "Distance between "+str(file_combinations[count][0])+" and "+str(file_combinations[count][1])+" is :"+str(dist)
	count = count + 1


somma_list = []

for key in distance_dict:
	somma = sum(distance_dict[key])
	somma_list.append(somma)
	if minimum is None or float(somma) < minimum:
		minimum = somma
		prototype = key
	if maximum is None or float(somma) > maximum:
		maximum = somma
		prototype_max = key
media_somma = (sum(somma_list)/len(somma_list))
print("PROTOTYPE: "+str(prototype)+"with sum distances of : "+str(minimum))
print("PROTOTYPE: "+str(prototype_max)+"with sum distances of : "+str(maximum))


print("La distanza media intracluster :"+str(media_somma))
