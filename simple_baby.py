#!/usr/bin/python

import random
import sys
import pprint


if (len(sys.argv) != 3):
    print "USAGE: simple_baby.py number_of_families max_family_size"
    sys.exit(1)


try:
   numberOfFamilies = int(sys.argv[1])
   maxFamSize = int(sys.argv[2])
except ValueError:
   print("Inputs are not valid numbers")
   sys.exit(2)



# global counters 
totalBoys = 0
totalGirls = 0
familyHistogram = {}


# chance of boy
chanceOfBoy = 0.5


def doBaby(familySize):

	## bail on too large of family
    if (familySize > maxFamSize):
    	return

    global totalBoys
    global totalGirls
    global familyHistogram

    fs = familySize + 1

    if (random.random() <= chanceOfBoy):
    	totalBoys += 1

        if fs in familyHistogram:
            familyHistogram[fs] = familyHistogram[fs] + 1
        else:
            familyHistogram[fs] = 1

    else:
    	totalGirls += 1
    	doBaby(fs)

    
for x in range(0, numberOfFamilies):
	doBaby(0)

pp = pprint.PrettyPrinter(indent=4)
pp.pprint(familyHistogram)
print "Boys:", totalBoys
print "Girl:", totalGirls


