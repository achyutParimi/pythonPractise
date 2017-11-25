# -*- coding: utf-8 -*-
"""
Created on Sun Nov 19 12:04:50 2017

@author: aparimi
"""

import pandas as pd
familyDict = {
        'name'   : ['ram','jyo','sandy'],
        'sex'    : ['M', 'F', 'M'],
        'height' : [5.7,5.3,4.11],
        'age'    : [39, 36, 10],
        'weight' : [190,170,90],
        'ageClass':['Adult','Adult','Kid'],
        'profession' : ['Manager', 'Sr Engineer', 'Student'],
        'hobbies': ['cricket', 'Knitting', 'Chess'],
        'favFood': ['biriyani', 'chanaMasala', 'shahi Paneer']
        }
familyFrame = pd.DataFrame(familyDict)

print(familyFrame[['name', 'sex']])

#shape of familyFrame
familyFrame.shape

print('columns:-------')
print(familyFrame.columns)
print('Info:-----')
print(familyFrame.info)

familyFrame.iloc[0:3, 0:3]

#print a particular column with 
familyFrame.loc[0:3, 'sex']
print('------------------loc----------------------')
print(familyFrame.loc[:,'name'])
print('------------------iloc----------------------')
print(familyFrame.iloc[:,0])

print(familyFrame.loc[familyFrame.sex =='M',['name', 'age', 'height', 'weight', 'profession', 'hobbies','favFood']])


familyFrame.loc[(familyFrame.ageClass =='Adult') & (familyFrame.age > 35) ,['name', 'age', 'height', 'weight', 'profession', 'hobbies','favFood']]

familyFrame.to_excel('d://Python/parimiFamily.xls')


