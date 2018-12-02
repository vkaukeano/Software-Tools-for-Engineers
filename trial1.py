import pandas as pd
from collections import defaultdict



def getGenre(file_name):
	#df = Data Frame => panda's version of an excel spreadsheet
	df = pd.read_csv(file_name)

	#creates dictionaries based on row names and values in column "genre". G1 is new dictionary
	G1 = df.groupby('genre1').genre1.count().to_dict()
	G2 = df.groupby('genre2').genre2.count().to_dict()
	G3 = df.groupby('genre3').genre3.count().to_dict()


	#declares a dictionary with values type list called "G"
	G = defaultdict(list)


	#combines all three columns per genre into single list and adds to dictionary called G
	for d in (G1, G2, G3):
		for key, value in d.iteritems():
			G[key].append(value)



	#declares regular dictionary Genre from collections dictionary G for summation purposes
	Genre = dict(G)


	#sums lists in dictionary G to get one value for sum for each genre
	for key in Genre:
		f = Genre.get(key)
		b = sum(f)
		Genre[key] = b

	print(Genre)
	return Genre


