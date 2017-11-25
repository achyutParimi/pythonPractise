# -*- coding: utf-8 -*-
"""
Created on Thu Nov 23 14:11:20 2017

@author: aparimi
"""

# Definition of countries and capital
print("How to relate 2 lists")
countries = ['spain', 'france', 'germany', 'norway']
capitals = ['madrid', 'paris', 'berlin', 'oslo']

# Get index of 'germany': ind_ger
ind_ger=countries.index('germany')

# Use ind_ger to print out capital of Germany
print(capitals[ind_ger])

print("Using DIctionaries")
# Definition of countries and capital
countries = ['spain', 'france', 'germany', 'norway']
capitals = ['madrid', 'paris', 'berlin', 'oslo']

# From string in countries and capitals, create dictionary europe
europe = {
    'spain': "madrid", 
    'france' : "paris", 
    'germany': "berlin", 
    'norway' : 'oslo'
}

# Print europe
print(europe)
print("European Countries: ", europe.keys())

print("European Capitals: ", europe.values())


print("Captial of Spain: ", europe.get('spain'))


#Add a new entry to a dictionary

europe['russia']='moscow'
print("European Countries/ Capitals: ", europe.items())
europe['india']='delhi'
print("European Countries/ Capitals: ", europe.items())
print('india' in europe)
del(europe['india'])
print("European Countries/ Capitals: ", europe.items())
print('india' in europe)


europe = { 'spain': { 'capital':'madrid', 'population':46.77 },
           'france': { 'capital':'paris', 'population':66.03 },
           'germany': { 'capital':'berlin', 'population':80.62 },
           'norway': { 'capital':'oslo', 'population':5.084 } }

# Print out the capital of France
print(europe['france']['capital'])

# Create sub-dictionary data

data = {'capital': 'rome', 'population': 59.83}

# Add data to europe under key 'italy'
europe['italy'] = data


# Print europe
print(europe)