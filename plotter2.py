import numpy as np
import matplotlib.pyplot as plt

def plotter2(xList, yList, title, xaxis):
	N = len(xList)
	ind = np.arange(N)
	width = 0.3
	
	#fig = plt.figure()
	#ax = fig.add_subplot(111)

	yvals = np.array(yList)
	rects1 = plt.bar(ind, yvals, width, color='b')

	#zvals = np.array(list(Dict2.values()))
	#rects2 = ax.bar(ind+width, zvals, width, color='r')
	
	plt.ylabel('Number of Movies')
	plt.xticks(ind+width, xList, rotation=30)

	plt.xlabel(xaxis)
	plt.title(title)

	plt.show()
