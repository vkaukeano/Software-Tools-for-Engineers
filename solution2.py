#!/usr/bin/env python
import random
import cProfile

from memory_profiler import profile

@profile
def FindDuplicates(numbers):
	dupVals = []
	for i in range(0, len(numbers)):
		for j in range(i+1, len(numbers)):
			if numbers[j] == numbers[i] and numbers[j] not in dupVals:
				dupVals.append(numbers[j])
	return len(dupVals)

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