#!/usr/bin/env python
import pandas as pd
from collections import defaultdict

#df = Data Frame => panda's version of an excel spreadsheet                                   
df = pd.read_csv('cleaned_data.csv')

# change to low_budget_csv.csv

df2 = pd.read_csv('high_budget_csv.csv')
#creates dictionaries based on row names and values in column "genre". D1 is new dictionary
 
D1 = df.groupby('director').director.count().to_dict()
D2 = df2.groupby('director').director.count().to_dict()


shared = set(D1.keys()) & set(D2.keys())

for key,value in shared:
    if  value <= 2:
        print key, '< 2'
    if 2 < value <= 5 :
        print key,'<= 5'
    if 5 < value <= 10:
        print key,'<=10'
    if 10 < value <= 15:
        print key,'<=15'
    if 15 < value <= 20:
        print key,'<=20'
    if value > 20:
        print key ,'>20'
