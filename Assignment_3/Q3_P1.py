
# coding: utf-8

# # Q3_P1
#  
# 1.Use ‘cricket_matches’ data set.
# 
# 2.Calculate the average score for each team which host the game and win the game.
#  
# 3.Remember that if a team hosts a game and wins the game, their score can be innings_1 runs or innings_2 runs. You have to check if the host team won the game, check which innings they played in (innings_1 or innings_2), and take the runs scored in that innings. The final answer is the average score of each team satisfying the above condition.
# 
# 4.Display a few rows of the outputuse df.head()

# In[7]:

import csv, sys
from pandas import Series, DataFrame
import pandas as pd
import numpy as np


# In[8]:

df = pd.read_csv('E:/Python/Data_Assignment_3/cricket_matches.csv')


# In[9]:

df.head()


# In[10]:

df1=df[['home','winner','innings1','innings1_runs','innings2','innings2_runs']] # considering only the required columns


# In[11]:

df1.head()


# In[12]:

#winner=1 else 0
df1['HOME'] = np.where(df1['home']==df1['winner'],'1','0')
df1.head()


# In[17]:

df2['score'] = np.where(df2['home']==df2['innings1'], df2['innings1_runs'], df2['innings2_runs'])


# In[18]:

df2.head()


# In[20]:

df3 = df2[['home','score']]
df3['score'] = df3.groupby(['home'])['score'].transform('mean')
df3.head()


# In[21]:

df3.to_csv('Q3_P1_output.csv') 


# In[ ]:



