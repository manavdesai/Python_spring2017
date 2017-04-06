
# coding: utf-8

# # Q2_P2:
# 1.Use 'employee_compensation' data set.
# 2.Find the people whose overtime salary is greater than 5% of salaries (salaries refers to ’Salaries' column)
# 3.For each job family these people are associated with (job family refers to ’Job Family' column), calculate what is the percentage of total benefits with respect to total compensation (so for each job family you have to calculate average total benefits and average total compensation). Create a new column (Percent_total_benefit) which has the percentage value.
# 4.Display the top 5 job families according to Percent_total_benefit using df.head().
# 5.Write the output (jobs and Percent_total_benefit) to a csv.

# In[1]:

import pandas as pd
import numpy as np
import csv


# In[2]:

df = pd.read_csv('E:/Python/Data_Assignment_3/employee_compensation.csv') 
df.head()


# In[15]:

df1 = df[['Year Type', 'Job Family', 'Employee Identifier', 'Salaries', 'Overtime', 'Total Salary', 'Total Benefits', 'Total Compensation']]
df2 = df1[df1['Year Type'] == 'Calendar']
df3 = df2.groupby(['Job Family', 'Employee Identifier'], as_index= False).mean()
df4 = df3[df3['Overtime']> 0.05* df3['Salaries']]
df5 = df4[['Job Family', 'Total Benefits', 'Total Compensation']]
df6 = df5.groupby(['Job Family'], as_index= False).mean() #Average
df6["Percent_Total_Benefit"] = 100* df6['Total Benefits']/df6['Total Compensation'] #Calculating percentage
df7= df6.sort_values(['Percent_Total_Benefit'], ascending = [False])


# In[16]:

df7.head()


# In[17]:

df7.to_csv('Q2_P2_output.csv')


# In[ ]:



