# -*- coding: utf-8 -*-
"""
Created on Fri Nov 24 11:08:12 2017

@author: aparimi
"""
import pandas as pd

dict = {
        "country" : ["Brazil", "Russia", "India", "China", "South Africa"],
        "capital" : ["Brasillia", "Moscow","New Delhi", "Beijing", "Pretoria"],
        "area" : [8.516, 17.10, 3.286, 9.597, 1.221],
        "population": [200.4, 143.5, 1252, 1357, 52.98]
        
        }

print("dictionaryFormat: ", dict)
dict.items()
dict.values()

brics = pd.DataFrame(dict)
print("dataFrame Format: ", brics)
print(len(brics))
brics.index = ["BR","RU","IN", "CH", "SA"]
print(brics)

brics.to_csv("D://Python/brics.csv")


bricks = pd.read_csv("D://Python/brics.csv", index_col=0)

print(bricks)

#Difference between single brackets vs double brackets
country = bricks[['country']]
print(country)
len(country)
print(type(country))

country = bricks['country']
print(country)
#print(type(country))
print(type(bricks['country']))

#Slicing: it is obtaining row information
#Column retrieval is done through loc & iloc
df = bricks[1:4]
print(df)

