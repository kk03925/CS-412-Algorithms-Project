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
	
	inputSizes = inputs.keys().sort()

	# Setting labels for the graphs
	p.ylabel("Running time in milliseconds")
	p.xlabel("Input size in number of points")

	# algo1

	# List to store execution times
	# for different input sizes (n values)
	algo1ExecTimes = [] 

	for n in inputs:
		print("Running algo1 for input size: " + str(n) + " ...")
		
		startTime = t.clock()
		# algo1(inputs[n])
		endTime = t.clock()	
		
		# Storing execution time for n points to plot
		algo1ExecTimes.append(endTime - startTime)

	# plotting and showing
	print("Plotting ...")
	p.plot(inputSizes, algo1ExecTimes, 'r')
	p.title("algo1 Running Time")
	p.show()

	# algo2

	# List to store execution times
	# for different input sizes (n values)
	algo2ExecTimes = [] 

	for n in inputs:
		print("Running algo2 for input size: " + str(n) + " ...")
		
		startTime = t.clock()
		# algo2(inputs[n])
		endTime = t.clock()	
		
		# Storing execution time for n points to plot
		algo2ExecTimes.append(endTime - startTime)

	# plotting and showing
	print("Plotting ...")
	p.plot(inputSizes, algo2ExecTimes, 'g')
	p.title("algo2 Running Time")
	p.show()

	# algo3

	# List to store execution times
	# for different input sizes (n values)
	algo3ExecTimes = [] 

	for n in inputs:
		print("Running algo3 for input size: " + str(n) + " ...")
		
		startTime = t.clock()
		# algo3(inputs[n])
		endTime = t.clock()	
		
		# Storing execution time for n points to plot
		algo3ExecTimes.append(endTime - startTime)

	# plotting and showing
	print("Plotting ...")
	p.plot(inputSizes, algo3ExecTimes, 'b')
	p.title("algo3 Running Time")
	p.show()

	# All algorithms

	# plotting and showing
	print("Plotting for all algorithms...")
	p.plot(inputSizes, algo1ExecTimes, 'r')
	p.plot(inputSizes, algo2ExecTimes, 'b')
	p.plot(inputSizes, algo3ExecTimes, 'g')
	p.title("Running Time For All Algorithms")
	p.legend(["algo1", "algo2", "algo3"])
	p.show()
	

if __name__ == '__main__':
    main()

