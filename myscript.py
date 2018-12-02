#!/usr/bin/env python                                          

import os
import sys

def main(argv):

    for root, dir, files in os.walk(sys.argv[1]):
        print "root = ", root
        print "dir = ", dir
        print "files = ", files

        with open(files) as f:
            for line in f:
                if line == "hyperventilation":
                    print  files
# begin gracefully                                            \
                                                               
#                                                             \
                                                               
if __name__ == "__main__":
    main(sys.argv[0:])

#                                                             \
                                                               
# end of file  
