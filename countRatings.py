#!/usr/bin/env python

import math
import csv

def countRatings(file_d):

    column = 'Rating'

    xr0=xr1=xr2=xr3=xr4=xr5=xr6=xr7=xr8=xr9=0;

    
    with open(file_d,'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            val = float(row[column])
            num = math.floor(val)
            if num < 1:
                xr0 += 1
            elif num >= 1 and num < 2:
                xr1 += 1
            elif num >= 2 and num < 3:
                xr2 += 1
            elif num >= 3 and num < 4:
                xr3 += 1
            elif num >= 4 and num < 5:
                xr4 += 1
            elif num >= 5 and num < 6:
                xr5 += 1
            elif num >= 6 and num < 7:
                xr6 += 1
            elif num >= 7 and num < 8:
                xr7 += 1
            elif num >= 8 and num < 9:
                xr8 += 1
            elif num >= 9 and num < 10:
                xr9 += 1
            
    ListR = [xr0,xr1,xr2,xr3,xr4,xr5,xr6,xr7,xr8,xr9]
    return ListR

