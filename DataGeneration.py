# Settings
# Note: please only tweak these values

# x axix
XMIN = -5000
XMAX = 5000

# y axis
YMIN = -5000
YMAX = 5000

# n range
NMIN = 10
NMAX = 5000
NINTERVAL = 10

# =============

# Main code

import numpy.random as r

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
		for point in range(n):
			
			# generating random point
			x = r.randint(XMIN, XMAX + 1)
			y = r.randint(YMIN, YMAX + 1)

			while ([x, y] in inputs[n]):
				x = r.randint(XMIN, XMAX + 1)
				y = r.randint(YMIN, YMAX + 1)

			# adding to list of points
			inputs[n].append([x, y])

	return inputs


def _Test():
	# "Private" function for testing 

	data = DataGeneration()

	for n in data:
		print(str(n) + " points: " + str(data[n]) + "\n")  


if __name__ == '__main__':
    _Test()