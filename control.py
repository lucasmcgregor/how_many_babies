#!/usr/bin/python

import random
import sys

if (len(sys.argv) != 2):
	print "USAGE: control.py number_of_runs"
	sys.exit(1)


try:
	numberOfRuns = int(sys.argv[1])
except ValueError:
	print("Inputs are not valid numbers")
	sys.exit(2)

# global counters 
totalBoys = 0
totalGirls = 0

# chance of boy
chanceOfBoy = 0.5

def doBaby():
	global totalBoys
	global totalGirls

	totalBoys=0
	totalGirls=0

	for x in xrange(0, numberOfRuns):
		if (random.random() <= chanceOfBoy):
			totalBoys += 1
		else:
			totalGirls += 1

print "Boys, Girls"
for x in xrange(0, 10):
	doBaby()
	print "%d, %d" % (totalBoys, totalGirls)
