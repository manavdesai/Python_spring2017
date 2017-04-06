
# coding: utf-8

# ## Q1_P2:
# 
# 1.Use ‘vehicle_collisions’ data set.
# 2.For each borough, find out distribution of each collision scale. (One car involved? Two? Three? or more?) (From 2015 to present)
# 3.Display a few rows of the output use df.head().
# 4.Generate a csv output with five columns ('borough', 'one-vehicle', 'two-vehicles', 'three-vehicles', 'more-vehicles')

# In[1]:

from pandas import Series, DataFrame 
import pandas as pd
import numpy as np


# In[2]:

df = pd.read_csv('E:/Python/Data_Assignment_3/vehicle_collisions.csv')


# In[3]:

df.head()


# In[22]:

df1 = df.groupby(['BOROUGH'],sort = False)['VEHICLE 1 TYPE','VEHICLE 2 TYPE','VEHICLE 3 TYPE','VEHICLE 4 TYPE'].count().reset_index()


# In[23]:

df1.head()


# In[24]:

df2= DataFrame()


# In[25]:

df2['BOROUGH'] = df1['BOROUGH']  
df2['1_Vehicle_Involved'] = df1['VEHICLE 1 TYPE'] - df1['VEHICLE 2 TYPE'] 
df2['2_Vehicles_Involved'] = df1['VEHICLE 2 TYPE'] - df1['VEHICLE 3 TYPE'] 
df2['3_Vehicles_Involved'] = df1['VEHICLE 3 TYPE'] - df1['VEHICLE 4 TYPE'] 
df2['N_Vehicles_Involved'] = df1['VEHICLE 4 TYPE'] 
df2.set_index('BOROUGH', inplace = True)


# In[26]:

df2.head()


# In[27]:

df2.to_csv('Q1_P2_output.csv')


# In[ ]:



