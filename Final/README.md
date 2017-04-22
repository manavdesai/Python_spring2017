
![ipl-logo](https://cloud.githubusercontent.com/assets/25045817/25302244/09900832-2708-11e7-9585-279805797ce8.png)

# Indian Premier League - OPEN DATA ANALYSIS
## Content
* Introduction
* Analysis-1 : Analysis on batsman
* Analysis-2 : Comparison of Players
* Analysis-3 : Analysis on bowlers
* Analysis-4 : Team-based analysis
* Analysis-5 : Toss-based analysis
## Introduction

The Indian Premier League (IPL) is a professional Twenty20 cricket league in India contested during April and May of every year by teams representing Indian cities. There are different teams with different players from different countries playing against each other to win IPL cup. The dataset represents information on different players, their performance, wickets and victory.

Using the dataset of this cricket league, I have performed analysis and asnwered various questions that may be helpful in future for the prediction or to determine the consistency of a player, team or a match. 

To support this, I have presented the data in terms of different graphs to better visualize the flow and existence of the data. 

In this Project, I have explored the data of Indian Premier League (IPL) which includes 2 files:

* matches.csv
* deliveries.csv 

Data is collected from http://cricsheet.org/

~ matches.csv consists of following columns & data for all 577 matches held till date

~ deliveries.csv consists of following columns & ball by ball data for each match held till date


#### Sample code to read csv data into a data frame.
```python 
sample code:
path=os.getcwd()
path=path+'\\Original_Data\\'
df_matches= pd.read_csv(path + "matches.csv")
df_deliveries= pd.read_csv(path + "deliveries.csv")
df_matches.head()
```

***************************************************************************************************************************************
## Analysis-1 : Analysis on batsman

In this analysis, I have integrated the facts related to a batsman and how it relates to his performance. Considering the number of runs scored by the batsman, his performance has been tracked over the years. The number of FOURS and SIXES hit by a batsman is analyzed and also to consider the number of dot balls given by batsman.
### Analysis 1.1 : Top Run scorers
#### Sample Code
```python
runs_df = df_deliveries.groupby('batsman')['batsman_runs'].agg('sum').reset_index().sort_values(by='batsman_runs', ascending=False).reset_index(drop=True)
runs_df = runs_df.iloc[:10,:]

```
<img width="582" alt="top_run_scorers" src="https://cloud.githubusercontent.com/assets/25045817/25302728/e84f1cd4-2712-11e7-8e33-2a9f5b865448.PNG">

### Conclusion
##### ~ V Kohli is the top run scorer amongst all followed by SK Raina.
##### ~ CH Gayle and DA Warner are highest run scorers in foreign players.
************************************************************************************************************************************
### Analysis 1.2 : Performance of Top 5 Batman over the seasons
#### Sample Code
```python
top=df_batsman.groupby(['season','batsman'])['batsman_runs'].sum().reset_index()
top=top.groupby(['season','batsman'])['batsman_runs'].sum().unstack().T
top['Total']=top.sum(axis=1)
top=top.sort_values(by='Total',ascending=0)[:5]
top.drop('Total',axis=1,inplace=True)
top.T.plot(figsize=(12,7))
plt.show()

```
<img width="557" alt="performance_by_batsman" src="https://cloud.githubusercontent.com/assets/25045817/25302757/9ac15e04-2713-11e7-9428-0351306708aa.PNG">

### Conclusion  
##### ~ V Kohli shows a considerable improved performance in the year 2016
##### ~ CH Gayle had good performance from 2011 to 2013 but then showed a drop
##### ~ SK Raina and RG Sharma had nearly consistent performance all the seasons
************************************************************************************************************************************
### Analysis 1.3 : Players with maximum number of 4's
#### Sample Code
```python
fours_df = df_deliveries.groupby('batsman')['batsman_runs'].agg(lambda x: (x==4).sum()).reset_index().sort_values(by='batsman_runs', ascending=False).reset_index(drop=True)
fours_df = fours_df.iloc[:10,:]
fours_df.head()

```
<img width="507" alt="players_with_4s" src="https://cloud.githubusercontent.com/assets/25045817/25302971/4eef6962-2718-11e7-826a-f2b8f4accc4e.PNG">

### Conclusion 
##### ~  G Gambhir has hit maximum number of FOURS. Total of 422 Fours
************************************************************************************************************************************
### Analysis 1.4 : Players with maximum number of 6's
#### Sample Code
```python
six_df = df_deliveries.groupby('batsman')['batsman_runs'].agg(lambda x: (x==6).sum()).reset_index().sort_values(by='batsman_runs', ascending=False).reset_index(drop=True)
six_df = six_df.iloc[:10,:]
six_df.head()

```
<img width="498" alt="players_with_6s" src="https://cloud.githubusercontent.com/assets/25045817/25303101/0bb24c94-271a-11e7-865e-72490cb8fc14.PNG">

### Conclusion 
##### ~ CH Gayle has hit maximum number of SIXES. Total 252 Sixes. 
