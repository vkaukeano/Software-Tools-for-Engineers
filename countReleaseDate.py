#!/usr/bin/env python
import csv
def countReleaseDate(file_d):

    column = 'release_date'

    xr1=xr2=xr3=xr4=xr5=xr6=xr7=xr8=xr9=xr10=xr11=xr12=0;
 
    with open(file_d,'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            
            val = row[column]
            val = ''.join([i for i in val if not i.isdigit()])
            
            if val == '-Jan-':
                xr1 += 1
            elif val == '-Feb-':
                xr2 += 1
            elif  val == '-Mar-':
                xr3 += 1
            elif val == '-Apr-':
                xr4 += 1
            elif val == '-May-':
                xr5 += 1
            elif val == '-Jun-':
                xr6 += 1
            elif val == '-Jul-': 
                xr7 += 1
            elif val == '-Aug-':
                xr8 += 1
            elif val == '-Sep-':
                xr9 += 1
            elif val == '-Oct-':
                xr10 += 1
            elif val == '-Nov-':
                xr11 += 1
            elif val == '-Dec-':
                xr12 += 1
            
    listR = [xr1,xr2,xr3,xr4,xr5,xr6,xr7,xr8,xr9,xr10,xr11,xr12]

    return listR

#
# end of file  
