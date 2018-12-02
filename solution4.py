#!/usr/bin/env python
import random
import cProfile

from memory_profiler import profile

@profile
def FindDuplicates(numbers):
	x=[]
	for n in set(numbers):
		count = numbers.count(n)
	if count > 1:
		x.append(n)
	return (len(x))

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