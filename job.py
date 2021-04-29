# -*- coding: utf-8 -*-
"""
Created on Tue Apr  6 17:37:52 2021

@author: marlon
"""

import pandas as pd
import matplotlib.pyplot as plt


def print_chart(labels, values):
    y_pos = range(len(labels))
    plt.bar(y_pos, values)
    # Rotation of the bars names
    plt.xticks(y_pos, labels, rotation=90)


df = pd.read_csv('titles.csv')

df = df.dropna(subset=['cast', 'country'])


df = df[df['country'].str.contains("United States")]

cast_list_cleared = []

for item in df['cast']:
    cast_list = item.split(',')    
    for actor in cast_list:
        if actor[0] == ' ':
            cast_list_cleared.append(actor[1:])
        else:
            cast_list_cleared.append(actor)
            

df = pd.DataFrame(data=cast_list_cleared, columns = ['actors'])    

 
print_chart(df['actors'].value_counts().head(20).index, df['actors'].value_counts().head(20).values)
