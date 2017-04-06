
# coding: utf-8

# #Q2_P1:
#     
# 1.Use 'employee_compensation' data set.
# 2.Find out the highest paid departments in each organization group by calculating mean of total compensation for every department.
# 3.Output should contain the organization group and the departments in each organization group with the total compensation from highest to lowest value.
# 4.Display a few rows of the output use df.head().

# In[1]:

import pandas as pd   
from pandas import DataFrame


# In[3]:

df = pd.read_csv('E:/Python/Data_Assignment_3/employee_compensation.csv')


# In[4]:

df.head()


# In[5]:

#calculating the average compensation
df1 = df.groupby(['Organization Group', 'Department'])['Total Compensation'].mean().reset_index().sort_values(["Organization Group","Total Compensation"],ascending=[True,False])
df1.set_index('Organization Group',inplace = True)
df1.head()


# In[6]:

df1.to_csv('Q2_P1_output.csv') 


# In[ ]:



