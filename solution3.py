#!/usr/bin/env python
import random
import cProfile

from memory_profiler import profile

@profile
def FindDuplicates(numbers):
	temp = []
	foo = 0
	numberz = set(numbers)
	for num in numberz:
		temp.append(numbers.count(num))
	for num in temp:
		if num > 1:
			foo += 1
	return foo

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