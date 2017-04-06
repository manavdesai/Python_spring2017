
# coding: utf-8

# # Q4_P4
#  
# 1.Use ‘movies_awards’ data set.
# 2.You are supposed to extract data from the awards column in this dataset and split it into several columns. An example is given below.
# 3.The awards has details of wins, nominations in general and also wins and nominations in certain categories(e.g. Oscar, BAFTA etc.)
# 4.You are supposed to create a win and nominated column (these 2 columns contain total number of wins and nominations) and other columns that extract the number of wins and nominations for each category of award. 
# 5.If a movie has 2 Oscar nominations and 4 Oscar won, the columns Oscar_Awards_Won should have value 4 and Oscar_Awards_Nominated should have value 2. You should also have a total won and nominated column which aggregates all the awards (won or nominated). 
# 6.Create two separate columns for each award category (won and nominated).

# In[10]:

import pandas as pd 
import csv
import datetime
import calendar
from pandas import read_csv
import re
import numpy as np


# In[11]:

df = pd.read_csv('E:/Python/Data_Assignment_3/movies_awards.csv')


# In[12]:

df.head()


# In[13]:

#Required columns
df1=df[['Title','Awards']]
df1=df1.dropna()
df1.head()


# In[14]:

df1["Wins"] = df1["Awards"].apply(lambda x : (re.findall(r"(\d+) win", x)))
df1["Nominations"] = df1["Awards"].apply(lambda x : (re.findall(r"(\d+) nomination", x)))
df1["Golden Globes Won"] = df1["Awards"].apply(lambda x : (re.findall(r"Won (\d+) Golden", x)))
df1["Golden Globes Nominated"] = df1["Awards"].apply(lambda x : (re.findall(r"Nominated for (\d+) Golden", x)))
df1["Oscars Nominated"] = df1["Awards"].apply(lambda x : (re.findall(r"Nominated for (\d+) Oscar", x)))
df1["Oscars Won"] = df1["Awards"].apply(lambda x : (re.findall(r"Won (\d+) Oscar", x)))
df1["Bafta Nominated"] = df1["Awards"].apply(lambda x : (re.findall(r"Nominated for (\d+) BAFTA", x)))
df1["Bafta Won"] = df1["Awards"].apply(lambda x : (re.findall(r"Won (\d+) BAFTA", x)))
df1["PrimeTime Won"] = df1["Awards"].apply(lambda x : (re.findall(r"Won (\d+) Primetime", x)))
df1["PrimeTime Nominated"] = df1["Awards"].apply(lambda x : (re.findall(r"Nominated for (\d+) Primetime", x)))


# In[15]:

df1.head()


# In[16]:

df1.to_csv('Q4_P1_output.csv') 


# In[ ]:



