#!/usr/bin/env python
import random
import cProfile

from memory_profiler import profile

@profile
def FindDuplicates(numbers):
	counter = 0
	if len(numbers) < 2:
		return counter
	else:
		numbers.sort()
		dup = 0
		for i in range(1,len(numbers)):
			if ((numbers[i-1] == numbers[i]) & (dup == 0)):
				counter = counter + 1
				dup = 1
			elif numbers[i-1] != numbers[i]:
				dup = 0
	# exit function and return number of unique duplicates 
	# 
	return counter

# begin gracefully
#
if __name__ == "__main__":

	numbers = []

	for i in range(1000000):
		value = random.randint(1, 40000)
		numbers.append(value)

	FindDuplicates(numbers)
#
# end of file