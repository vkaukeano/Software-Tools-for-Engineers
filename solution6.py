#!/usr/bin/env python
import random
import cProfile

from memory_profiler import profile

@profile
def FindDuplicates(numbers):
	allDupes = [x for x in numbers if numbers.count(x) >= 2]
	uniqueDupes = list(set(allDupes))
	numberOfDupes = len(uniqueDupes)
	return numberOfDupes

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