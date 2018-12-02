#!/usr/bin/env python

# import required modules:
#  note that the path to the module htkmfc must be included in the
#  PYTHONPATH environment variable.
#
import os
import sys

# main: this is the main function of this Python
#
def main(argv):

    for root, dir, files in os.walk(sys.argv[1]):
        print "root = ", root
        print "dir = ", dir
        print "files = ", files

# begin gracefully
#
if __name__ == "__main__":
    main(sys.argv[0:])

#
# end of file
