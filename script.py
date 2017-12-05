#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec  1 13:45:33 2017

@author: Achuth Arun Resmi
"""
#%%
#Importing required packages

import pandas as pd

#%%
#Data Preparation

df_train = pd.read_csv('/Users/achuth/Downloads/Kaggle/train.csv', sep = ',')

#df_train['Fare'] = round(df_train['Fare'], 2)
#names = df_train.columns.tolist()
#del names[1]
#sur = df_train['Survived']
#df_train = df_train[names]
#df_train['Survived'] = sur
#del names, sur

#%%
#Extracting Deck of each passenger

deck = df_train['Cabin'].fillna(0).tolist()

for i in range(0,len(deck)):
    if deck[i] != 0:
        deck[i] = deck[i][:1]

df_train['Deck'] = deck

del deck, i, df_train['Cabin']

#%%
#Converting Fare into categorical variable

#test = pd.DataFrame({'Class': df_train['Pclass'],'Fare': df_train['Fare'], 'Port': df_train['Embarked'], 'Deck':df_train['Deck'], 'Survived':df_train['Survived']})
#test_unique = test.groupby(['Class','Port', 'Deck', 'Fare', 'Survived']).size().reset_index().rename(columns={0:'Count'})

bin_labels = ['1st Quartile', '2nd Quartile', '3rd Quartile', '4th Quartile']
quartiles = pd.qcut(df_train['Fare'], 4, labels = bin_labels)
df_train['Fare'] = quartiles
del quartiles, bin_labels

#%%
#Converting Name variable into Last Name and Married
lastname = []
for i in range(0, len(df_train['Name'])):
    lastname.append(df_train['Name'][i].split(',')[0])
df_train['Last Name'] = lastname

del lastname, df_train['Name'], i

#%%
#Correcting Age

df_train.Age = df_train.Age.fillna(-0.5)
bins = (-1, 0, 5, 12, 18, 25, 35, 60, 120)
group_names = ['Unknown', 'Baby', 'Child', 'Teenager', 'Student', 'Young Adult', 'Adult', 'Senior']
df_train['Age'] = pd.cut(df_train['Age'], bins, labels = group_names)

del bins, group_names

#%%    

