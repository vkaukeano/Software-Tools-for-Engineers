#!/usr/bin/env python
import random
import cProfile

from memory_profiler import profile

@profile
def FindDuplicates(numbers):

	d = {}
	for val in numbers:
		d[val] = d.get(val, 0) + 1
	return sum(d[i] > 1 for i in d)

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