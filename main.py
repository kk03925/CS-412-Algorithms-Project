import time as t
import matplotlib.pyplot as p
import pandas as pd
from DataGeneration import DataGeneration
from giftwrapping import gift_wrapping
from graham_scan import graham_scan
from quickHull2 import quickHull
from pyhull.convex_hull import ConvexHull

# Settings
WINDOWSIZE = 10

def _Smoothen(numbers):
	# Function to smoothen graphs using
	# moving averages
	# Based on:
	# https://www.kite.com/python/answers/how-to-find-the-moving-average-of-a-list-in-python

	numberSeries = pd.Series(numbers)
	movingAverages = numberSeries.rolling(WINDOWSIZE, 1).mean()
	movingAveragesList = movingAverages.tolist()

	return movingAveragesList


def main():
	# Main function that generates data and uses 
	# it to find and plot execution time for all 
	# 3 algorithms separately and on the same figure
	# for comparison

	# Generating data
	print("Generating data ...")
	inputs = DataGeneration()
	
	inputSizes = sorted(inputs.keys())

	# gift_wrapping

	# List to store execution times
	# for different input sizes (n values)
	gift_wrappingExecTimes = []

	print("Running gift_wrapping for all input sizes in the dataset ...")
	for n in inputs:
		startTime = t.clock()
		gift_wrapping(inputs[n])
		endTime = t.clock()	
		
		# Storing execution time for n points
		gift_wrappingExecTimes.append(endTime - startTime)


	# smoothening 
	gift_wrappingExecTimes = _Smoothen(gift_wrappingExecTimes)

	# plotting and showing
	print("Plotting ...")
	p.plot(inputSizes, gift_wrappingExecTimes, 'r')
	p.ylabel("Running time in microseconds")
	p.xlabel("Input size in number of points")
	p.title("gift_wrapping Running Time")
	p.show()

	# graham_scan

	# List to store execution times
	# for different input sizes (n values)
	graham_scanExecTimes = [] 

	print("Running graham_scan for all input sizes in the dataset ...")
	for n in inputs:
		startTime = t.clock()
		graham_scan(inputs[n])
		endTime = t.clock()	

		# Storing execution time for n points
		graham_scanExecTimes.append(endTime - startTime)

	# smoothening 
	graham_scanExecTimes = _Smoothen(graham_scanExecTimes)

	# plotting and showing
	print("Plotting ...")
	p.plot(inputSizes, graham_scanExecTimes, 'g')
	p.ylabel("Running time in microseconds")
	p.xlabel("Input size in number of points")
	p.title("graham_scan Running Time")
	p.show()

	# quickHull

	# List to store execution times
	# for different input sizes (n values)
	quickHullExecTimes = [] 

	print("Running quickHull for all input sizes in the dataset ...")
	for n in inputs:
		qHObj = quickHull(inputs[n])

		startTime = t.clock()
		qHObj.quickHull()
		qHObj.finalHull
		endTime = t.clock()	
		
		# Storing execution time for n points
		quickHullExecTimes.append(endTime - startTime)

	# smoothening 
	quickHullExecTimes = _Smoothen(quickHullExecTimes)

	# plotting and showing
	print("Plotting ...")
	p.plot(inputSizes, quickHullExecTimes, 'b')
	p.ylabel("Running time in microseconds")
	p.xlabel("Input size in number of points")
	p.title("quickHull Running Time")
	p.show()

	# pyhull.convex_hull.ConvexHull (library function)

	# List to store execution times
	# for different input sizes (n values)
	ConvexHullExecTimes = [] 

	print("Running pyhull.convex_hull.ConvexHull (library function) for all input sizes in the dataset ...")
	for n in inputs:
		startTime = t.clock()
		ConvexHull(inputs[n]).vertices
		endTime = t.clock()	
		
		# Storing execution time for n points
		ConvexHullExecTimes.append(endTime - startTime)

	# smoothening 
	ConvexHullExecTimes = _Smoothen(ConvexHullExecTimes)

	# plotting and showing
	print("Plotting ...")
	p.plot(inputSizes, ConvexHullExecTimes, 'c')
	p.ylabel("Running time in microseconds")
	p.xlabel("Input size in number of points")
	p.title("pyhull.convex_hull.ConvexHull (library function) Running Time")
	p.show()

	# All algorithms

	# plotting and showing
	print("Plotting for all algorithms...")
	p.plot(inputSizes, gift_wrappingExecTimes, 'r')
	p.plot(inputSizes, graham_scanExecTimes, 'g')
	p.plot(inputSizes, quickHullExecTimes, 'b')
	p.plot(inputSizes, ConvexHullExecTimes, 'c')
	p.ylabel("Running time in microseconds")
	p.xlabel("Input size in number of points")
	p.title("Running Time For All Algorithms")
	p.legend(["gift_wrapping", "graham_scan", "quickHull", "pyhull.convex_hull.ConvexHull (library function)"])
	p.show()
	

if __name__ == '__main__':
    main()

