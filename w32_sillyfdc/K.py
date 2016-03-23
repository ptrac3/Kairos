from __future__ import print_function
import numpy as np


fname = 'lenght.txt'


import numpy
def median(lst):
    return numpy.median(numpy.array(lst))


def print_to_file(fname):
        with open(fname) as file:
                for line in file:
                        samples_number = len(line.split())
			line = line.rstrip()
			mediana = median([int(x) for x in line.split()])
			mediana = int(mediana)
			file_out = open(fname+"_mediana"+".dat", "a")
                        print(mediana, file = file_out)
			
family = "cryptolocker"
sample_load = [int(x) for x in open("./lenght.txt")]
sample_load_sort = sorted(sample_load, key=int)
print(str(sample_load_sort))
mediana = median([int(x) for x in sample_load_sort])

mediana = int(mediana)
print(str(mediana))
