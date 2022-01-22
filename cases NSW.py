# -*- coding: utf-8 -*-
"""
Created on Tue Aug 17 09:21:45 2021

@author: sean.deboo
"""

import pandas as pd
pd.plotting.register_matplotlib_converters()
import matplotlib.pyplot as plt
import seaborn as sns

weeklydata = pd.read_csv('data.csv', index_col='WE Dose %')
                         
plt.figure(figsize=(14,7))                         
plt.title("2nd Dose % by age group - NSW") 
plt.xlabel('Weekending Dose Coverage')                        
sns.heatmap(data=weeklydata[::2], annot=True, fmt='g', vmax=80, cmap='hot_r')
