# Settings
# Note: please only tweak these values

# x axix
XMIN = -1000
XMAX = 1000

# y axis
YMIN = -1000
YMAX = 1000

# n range
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

	for n in range(NMIN, NMAX + NINTERVAL, NINTERVAL):
		
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


def _Test():
	# "Private" function for testing 

	data = DataGeneration()

	for n in data:
		print(str(n) + " points: " + str(data[n]) + "\n")  


if __name__ == '__main__':
    _Test()