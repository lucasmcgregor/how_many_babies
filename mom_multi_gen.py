#!/usr/bin/python
#from __future__ import division

import random
import sys
import pprint




if len(sys.argv) != 5:
	print "USAGE mom_multi_gen.py number_of_families max_family_size number_of_generations generation_life_span"
	print "Example mom_multi_gen.py 1000000 5 100 3"
	sys.exit(1)

try:
	number_of_families = int(sys.argv[1])
	max_family_size = int(sys.argv[2])
	number_of_generations = int(sys.argv[3])
	generation_life_span = int(sys.argv[4])
except ValueError:
	print("Inputs are not valid integers")
	sys.exit(2)

# global counters
generations = []
current_gen_girl_total = 0
current_gen_boy_total = 0

# changeOfBoy
chance_of_boy = 0.5

def doBaby(family_size):

	## bail on too large of family
    if (family_size > max_family_size):
    	return

    global current_gen_girl_total
    global current_gen_boy_total
    global generations

    fs = family_size + 1

    if (random.random() <= chance_of_boy):
    	current_gen_boy_total += 1

    else:
    	current_gen_girl_total += 1
    	doBaby(fs)


def doGeneration(families_in_generation):
	global current_gen_girl_total
	global current_gen_boy_total
	global generations
	current_gen_girl_total = 0
	current_gen_boy_total = 0

	# do all the families for a generation
	for i in xrange(0, families_in_generation):
		doBaby(0)

	# record their total for this generation
	genData = {
		'boys':current_gen_boy_total,
		'girl':current_gen_girl_total,
		'total':(current_gen_boy_total+current_gen_girl_total)
	}

	generations.append(genData)	

# START WITH THE SEED NUMBER OF FAMILIES PER GEN
families_in_generation = number_of_families

print "Generation, Total Pop, Boys, Girls, Pct Boys"

for gen in xrange(0, number_of_generations):
	#print "Doing generation: %d" % gen

	doGeneration(families_in_generation)

	# ASSUME THE FEMALES ARE THE LIMITING RESOURCE PER GEN
	# EACH FEMALE CAN HAVE THE MAX NUMBER OF CHILDREN
	# SO UPDATE THE NUMBER OF FAMILIES TO MATCH THE PREVIOUS GENERATIONS
	# COUNT OF FEMALE OFFSPRING
	families_in_generation = current_gen_girl_total

	if (current_gen_girl_total > 0):
		pctBoy = float(current_gen_boy_total)/float(current_gen_boy_total+current_gen_girl_total)
	else:
		pctBoy = 0

	print "%d, %d, %d, %d, %f" % (gen, (current_gen_girl_total+current_gen_boy_total), current_gen_boy_total, current_gen_girl_total, pctBoy)
