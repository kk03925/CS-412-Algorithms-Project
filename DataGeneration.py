# Settings

XMIN = -1000
XMAX = 1000

YMIN = 1000
YMAX = 1000

NMIN = 100
NMAX = 1000
NINTERVAL = 100

# =============

# Main code

import random as r

def DataGeneration():
	# Function to generate data in the form of dictionary
	
	# {
	# minimum n: [list of minimum n points]
	# .
	# .
	# maximum n: [list of maximum n points]
	# } 

	inputs = {}

	for n in range(NMIN, NMAX, NINTERVAL):
		
		# creating list of n points
		inputs[n] = []

		# generating random n points
		for point in range(1, n + 1):
			
			# generating random point
			x = r.randint(XMIN, XMAX)
			y = r.randint(YMIN, YMAX)

			# adding to list of points
			inputs[n].append((x, y))

	return inputs
