import numpy as np
import matplotlib.pyplot as plt

def plotter(Dict1, title, key1,xaxis):
	N = len(list(Dict1.keys()))
	ind = np.arange(N)
	width = 0.3
	
	#fig = plt.figure()
	#ax = fig.add_subplot(111)

	yvals = np.array(list(Dict1.values()))
	rects1 = plt.bar(ind, yvals, width, color='b')

	#zvals = np.array(list(Dict2.values()))
	#rects2 = ax.bar(ind+width, zvals, width, color='r')
	
	plt.ylabel('Number of Movies')
	plt.xticks(ind+width, list(Dict1.keys()), rotation=30)

	plt.xlabel(xaxis)
	plt.title(title) 

	plt.xlabel(xaxis)

	plt.show()
