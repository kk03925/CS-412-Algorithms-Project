import time as t
import matplotlib.pyplot as p
# import pandas as pd
from DataGeneration import DataGeneration
from giftwrapping import gift_wrapping
from graham_scan import graham_scan
from quickHull2 import quickHull


# def _Smoothen(numbers):
# 	# Function to smoothen graphs using
# 	# moving averages

# 	window_size = len(numbers)

# 	numbers_series = pd.Series(numbers)
# 	windows = numbers_series.rolling(window_size)
# 	moving_averages = windows.mean()

# 	moving_averages_list = moving_averages.tolist()
# 	without_nans = moving_averages_list[window_size - 1:]

# 	return without_nans


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

	# Setting labels for the graphs
	p.ylabel("Running time in microseconds")
	p.xlabel("Input size in number of points")

	# List to store execution times
	# for different input sizes (n values)
	gift_wrappingExecTimes = [] 

	for n in inputs:
		print("Running gift_wrapping for input size: " + str(n) + " ...")
		
		startTime = t.clock()
		gift_wrapping(inputs[n])
		endTime = t.clock()	
		
		# Storing execution time for n points to plot
		gift_wrappingExecTimes.append(endTime - startTime)


	# # smoothening 
	# gift_wrappingExecTimes = _Smoothen(gift_wrappingExecTimes)

	# plotting and showing
	print("Plotting ...")
	p.plot(inputSizes, gift_wrappingExecTimes, 'r')
	p.title("gift_wrapping Running Time")
	p.show()

	# graham_scan

	# Setting labels for the graphs
	p.ylabel("Running time in microseconds")
	p.xlabel("Input size in number of points")

	# List to store execution times
	# for different input sizes (n values)
	graham_scanExecTimes = [] 

	for n in inputs:
		print("Running graham_scan for input size: " + str(n) + " ...")
		
		startTime = t.clock()
		graham_scan(inputs[n])
		endTime = t.clock()	
		
		# Storing execution time for n points to plot
		graham_scanExecTimes.append(endTime - startTime)

	# # smoothening 
	# graham_scanExecTimes = _Smoothen(graham_scanExecTimes)

	# plotting and showing
	print("Plotting ...")
	p.plot(inputSizes, graham_scanExecTimes, 'g')
	p.title("graham_scan Running Time")
	p.show()

	# quickHull

	# Setting labels for the graphs
	p.ylabel("Running time in microseconds")
	p.xlabel("Input size in number of points")

	# List to store execution times
	# for different input sizes (n values)
	quickHullExecTimes = [] 

	for n in inputs:
		print("Running quickHull for input size: " + str(n) + " ...")
		
		startTime = t.clock()
		quickHull(inputs[n])
		endTime = t.clock()	
		
		# Storing execution time for n points to plot
		quickHullExecTimes.append(endTime - startTime)

	# # smoothening 
	# quickHullExecTimes = _Smoothen(quickHullExecTimes)

	# plotting and showing
	print("Plotting ...")
	p.plot(inputSizes, quickHullExecTimes, 'b')
	p.title("quickHull Running Time")
	p.show()

	# All algorithms

	# plotting and showing
	print("Plotting for all algorithms...")
	p.plot(inputSizes, gift_wrappingExecTimes, 'r')
	p.plot(inputSizes, graham_scanExecTimes, 'g')
	p.plot(inputSizes, quickHullExecTimes, 'b')
	p.title("Running Time For All Algorithms")
	p.legend(["gift_wrapping", "graham_scan", "quickHull"])
	p.show()
	

if __name__ == '__main__':
    main()

