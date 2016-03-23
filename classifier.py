import time
import sys
import multiprocessing
import os
import numpy
from dtw import dtw
from os import listdir
from os.path import isfile, join
import glob
import random
from random import randint

start_time = time.time()


directory = "./cryptolocker/"
proto_dir = "./prototype/"
prototypes = ['vanti','swizzor','cryptolocker','zeus','reveton']
samples = r"./"+directory+"/test/"+"*.dat"
OK = 0
KO = 0

#print "       [   FAMILY   ] : [PREVISION]"

class_dict = {'w32_downadup':0,'w32_chir':0,'w32_xpaj':0,'swizzor':0,'vanti':0,'cryptolocker':0,'hamweq':0,'koobface':0,'reveton':0,'ghostrat':0,'zeus':0,'w32_ramnit':0,'w32_sillyfdc':0}

family = ''

for path in glob.glob(samples):
	dirname, filename = os.path.split(path)
        minimum = None
	filename_split = filename.split('-')
        sample_family = filename_split[1]
	filename2_split = sample_family.split('.')
	sample_family = filename2_split[0]
	for i in range(0, len(prototypes)):
		proto_load = [int(x) for x in open("./"+prototypes[i]+"/prototype/"+prototypes[i]+"-prototype.dat").readlines()]
        	sample_load = [int(x) for x in open("./"+directory+"/test/"+filename).readlines()]
		dist, cost, path = dtw(proto_load, sample_load)
		print("Distance between "+sample_family+" sample and "+prototypes[i]+" prototype is "+str(dist))
		if minimum is None or dist < minimum:
			minimum = dist
			name = filename
			family = prototypes[i]
	print "Sample ["+sample_family+"] : ["+family+"]  "+str(minimum),
	class_dict[family] = class_dict[family] + 1
	if family.lower() == sample_family.lower():
		print(" [OK]")
		#OK = OK + 1
	else:
		print(" [KO]")
		KO = KO + 1
	
#print "Il numero di OK e "+str(OK)
#print "Il numero di KO e "+str(KO)	

for key in class_dict:
	print("Family "+str(key)+" count : "+str(class_dict[key]))

elapsed_time = time.time() - start_time
print(elapsed_time)
