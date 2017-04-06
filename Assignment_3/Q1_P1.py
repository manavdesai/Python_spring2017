
# coding: utf-8

# ## Q1_P1:
# 
# 1.Use ‘vehicle_collisions’ data set.
# 2.For each month in 2016, find out the percentage of collisions in Manhattan out of that year's total accidents in New York City.
# 3.Display a few rows of the output use df.head().
# 4.Generate a csv output with four columns (‘Month’, ‘Manhattan’, ‘NYC’, ‘Percentage’)
# 

# In[1]:

import pandas as pd
from pandas import Series, DataFrame
import csv


# In[3]:

df = pd.read_csv('E:/Python/Data_Assignment_3/vehicle_collisions.csv') 


# In[4]:

df.head()


# In[5]:

df['Year'] = pd.to_datetime(df['DATE']).dt.year # extracting the year of all the data 
df['Month'] = pd.to_datetime(df['DATE']).dt.month # extracting the month of the data


# In[6]:

Year16 = df[df['Year']==2016] #extracting the data of the year 2016


# In[46]:

Year16


# In[47]:

ManhCountList=[]
ManhList=[]
PercList=[]
NYCList =[]

for i in range(1, 13):

    Month16 = Year16[Year16['Month']==i]
    TotalCount = Year16[Year16['Month']==i].count().Month
    Manhcount = Month16[Month16['BOROUGH']=='MANHATTAN'].count().BOROUGH
    Percent = Manhcount/TotalCount
    ManhList.append(i)
    ManhCountList.append(Manhcount)
    NYCList.append(TotalCount)   
    PercList.append(Percent)


# In[48]:

final = {'MONTH':ManhList,'MANHATTAN':ManhCountList,'NYC':NYCList,'PERCENTAGE':PercList}
df2 = DataFrame(final)


# In[49]:

df2.head()


# In[50]:

df2.to_csv('Q1_P1_output.csv')


# In[ ]:



