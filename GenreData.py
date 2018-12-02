from trial1 import getGenre
from plotter import plotter
import sys


Blockbuster = getGenre(sys.argv[1])

plotter(Blockbuster,'Low Budget Films', 'Blockbusters', 'Genre')
