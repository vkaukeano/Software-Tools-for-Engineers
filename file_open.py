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

    # first method
    #
    with open(sys.argv[1]) as f:
        for line in f:
            if (line[0] != '#'):
                print  line
    f.close()

# begin gracefully
#
if __name__ == "__main__":
    main(sys.argv[0:])

#
# end of file
