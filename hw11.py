#!/usr/bin/env python
# import required modules:
# note that the path to the module htkmfc must be included in the # PYTHONPATH environment variable.
#
from __future__ import division
import os
import sys
import argparse
import re
import fileinput
import operator
import time
import collections
import math
# main: this is the main function of this Python
#
def main(argv):
		start_time = time.time()
	parser = argparse.ArgumentParser(description="homework 11: calculates n-grams on lists of files containing a pattern")
	parser.add_argument('-ngram',type=int,help='arg of type int that is n for n-gram value')
	parser.add_argument('-pattern',help='pattern string that files are searched for')
	postparser = argparse.ArgumentParser(description="here are the lists")
	contain
	postparser.add_argument('list',help='these are list files which names of .txt files',nargs='*',action='store')
	args, remaining_args = parser.parse_known_args() args = postparser.parse_args(remaining_args, args)
	target = []
	N = args.ngram
	pat = args.pattern
	counter = 0
	b = []
#loop over list file and generate target list
#of files to be opened
#
	for i in args.list:
			print "this is a file: %s" %(i)  # do whatever
			with open(i, 'r') as f:
				target.extend(f.readlines())pat)
	target = [item.rstrip() for item in target]
#loop over target files looking for pattern
#
	for line in target:
			with open(line,"r") as f:
					for line2 in f:
							if re.search(pat,line2):
									b.append(line)
	counter += 1
	break
	print "A total of %d files contained the word %s." %(counter,
	print " "
#open files with pattern and put their text in str1
#
	str1 = ""
	for i in range(0, len(b)):
		with open(b[i], "r") as fp:
	for data in fp:
		str1 = str1 + data
#ngram function declarations to tokenize strings, #find ngrams and print ngrams below
#
	lengths}
	queue to dict
	queue = collections.deque(maxlen=max_length)
# Helper function to add n-grams at start of current
	def add_queue():
		current = tuple(queue)
	def tokenize(string):
		return re.findall(r'\w+', string.lower())
	def count_ngrams(lines, min_length=N, max_length=N):
	lengths = range(min_length, max_length + 1)
	ngrams = {length: collections.Counter() for length in
	for length in lengths:
								if len(current) >= length: ngrams[length][current[:length]] += 1
# Loop through all lines and words and add n-grams to dict
	for line in lines:
			for word in tokenize(line):
					queue.append(word)
					if len(queue) >= max_length:
	add_queue()
# Make sure we get the n-grams at the tail end of the
	queue
		while len(queue) > min_length:
				queue.popleft()
	add_queue()
		return ngrams
	def print_most_frequent(ngrams, num=10): x=0
	y=0
	for n in ngrams:
		x = x + sum(ngrams[n].itervalues())
		print "There are %s ngrams" %(x)
'.format(num, n))
	for n in sorted(ngrams):
		print('----- {} most common {}-grams -----
	for gram, count in ngrams[n].most_common(num): p = 100*count/x
	y=y+p
	print('{}: {} {}% {}%'.format(' print('')
#finding ngrams below
#
	str1 = tokenize(str1)
	'.join(gram), count, p,y))
	ngrams = count_ngrams(str1) print_most_frequent(ngrams)
	elapsed_time = time.time() - start_time print('Took {:.03f} seconds'.format(elapsed_time))
# begin gracefully
#
if __name__ == "__main__":
	main(sys.argv[1])
#
# end of file