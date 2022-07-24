# -*- coding: utf-8 -*-
"""
Created on Tue Jul  5 16:54:27 2022

@author: chery
"""

import pandas as pd
import plotly.express as px

# storing the dataset
data1 = input('testdata1')
data2 = input('testdata2')

# reading the data
dataRead1 = pd.read_excel(data1)
dataRead2 = pd.read_excel(data2)

#print(df_prices, df_home_1)
reference = input("What is the basis of merging?")
data_total = dataRead2.merge(dataRead1, on=reference)

# print(df_total)
criteria_1 = input("enter criteria 1")
criteria_2 = input("enter criteria 2")

fig = px.pie(data_total[[criteria_1, criteria_2]],
             values=criteria_2, names=criteria_1)
fig.show()
