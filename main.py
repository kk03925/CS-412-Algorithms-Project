import time as t
import matplotlib.pyplot as p
from DataGeneration import DataGeneration

def main():
	# Main function that generates data and uses 
	# it to find and plot execution time for all 
	# 3 algorithms separately and on the same figure
	# for comparison

	# Generating data
	inputs = DataGeneration()
	
	inputSizes = sorted(inputs.keys())

	# Setting labels for the graphs
	p.ylabel("Running time in milliseconds")
	p.xlabel("Input size in number of points")

	# gift_wrapping

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

	# plotting and showing
	print("Plotting ...")
	p.plot(inputSizes, gift_wrappingExecTimes, 'r')
	p.title("gift_wrapping Running Time")
	p.show()

	# graham_scan

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

	# plotting and showing
	print("Plotting ...")
	p.plot(inputSizes, graham_scanExecTimes, 'g')
	p.title("graham_scan Running Time")
	p.show()

	# KPS

	# List to store execution times
	# for different input sizes (n values)
	KPSExecTimes = [] 

	for n in inputs:
		print("Running KPS for input size: " + str(n) + " ...")
		
		startTime = t.clock()
		KPS(inputs[n])
		endTime = t.clock()	
		
		# Storing execution time for n points to plot
		KPSExecTimes.append(endTime - startTime)

	# plotting and showing
	print("Plotting ...")
	p.plot(inputSizes, KPSExecTimes, 'b')
	p.title("KPS Running Time")
	p.show()

	# All algorithms

	# plotting and showing
	print("Plotting for all algorithms...")
	p.plot(inputSizes, gift_wrappingExecTimes, 'r')
	p.plot(inputSizes, graham_scanExecTimes, 'b')
	p.plot(inputSizes, KPSExecTimes, 'g')
	p.title("Running Time For All Algorithms")
	p.legend(["gift_wrapping", "graham_scan", "KPS"])
	p.show()
	

if __name__ == '__main__':
    main()

