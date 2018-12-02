#from trial1 import getGenre
#from plotter import plotter
#from plotter2 import plotter2
import sys
#from countRatings import countRatings
#from countReleaseDate import countReleaseDate
from ratingsCounter import fractionRatings
from releaseDateCounter import releaseDates
from Directors import directorList

#StDv = fractionRatings(sys.argv[1], sys.argv[2])
#StDv2 = releaseDates(sys.argv[1], sys.argv[2])
StDv3 = directorList(sys.argv[1], sys.argv[2])
#by Genre
#lbBlockbuster = getGenre(sys.argv[1])
#plotter(lbBlockbuster,'Low Budget Blockbusters', 'Blockbusters', 'Genre')

#hbFailure = getGenre(sys.argv[2])
#plotter(hbFailure, 'High Budget Failures', 'Failures', 'Genre')



#by Rating
#LBBR = countRatings(sys.argv[1])
#HBBR = countRatings(sys.argv[2])
#Rating = ['0-1', '1-2', '2-3', '3-4', '4-5', '5-6', '6-7', '7-8', '8-9', '9-10']



#plotter2(Rating,lbBlockbusterR,'Low Budget Blockbusters', 'Rating Range')
#plotter2(Rating,hbFailureR,'High Budget Failures', 'Rating Range')



#by Time of Year
#lbBlockbusterT = countReleaseDate(sys.argv[1])
#hbFailureT =  countReleaseDate(sys.argv[2])
#Month = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']

#plotter2(Month,lbBlockbusterT, 'Low Budget Blockbusters', 'Month of Theatrical Release')
#plotter2(Month,hbFailureT, 'High Budget Failures', 'Month of Theatrical Release')




