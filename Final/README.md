
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
************************************************************************************************************************************
### Analysis 1.5 : Players with maximum number of Dot ball
#### Sample Code
```python
dot_df = df_deliveries.groupby('batsman')['batsman_runs'].agg(lambda x: (x==0).sum()).reset_index().sort_values(by='batsman_runs', ascending=False).reset_index(drop=True)
dot_df = dot_df.iloc[:10,:]
dot_df.head()

```
<img width="430" alt="players_with_dot_balls" src="https://cloud.githubusercontent.com/assets/25045817/25306956/6c55c7fa-2766-11e7-9501-82c7d4c2b052.PNG">

### Conclusion
##### ~ Surprisingly, V Kohli, who has scored the maximum runs is also the player with maximum DOT balls 

***************************************************************************************************************************************
***************************************************************************************************************************************
## Analysis-2 : Comparison of players.

In this analysis, <img width="256" alt="dhoni" align="right" src="https://cloud.githubusercontent.com/assets/25045817/25307103/453f2ae6-2769-11e7-9833-0a01870b3232.PNG">
I have compared the performances of two players and given the statistical data about their runs scored, the number of balls they faced and also the comparison based on the strike rate that they have over the seasons. This analysis is helpful if we want to make a comparison of the two players and conclude about their work. I have taken an instance of V kohli, who is the captain of Royal Challengers Bangalore AND MS Dhoni, who is the former captain of Chennai Super Kings and now playing for Pune Warriors. 


Both these players are the leads in Indian Cricket Team. Interesting part is to see how well is their IPL Career. Let's take a glance. 
##### ( Virat Kohli vs MS Dhoni )

#### Sample Code to integrate the data of Virat Kohli and MS Dhoni
```python
inputstring = 'V Kohli'
inputstring1 = 'MS Dhoni'
for i in [inputstring1, inputstring]:
      df_new = df_batsman.ix[df_batsman.ix[:,"batsman"].str.contains(str(i))]
df_player_comparison = df_batsman.ix[df_batsman.ix[:,"batsman"].str.contains(str(inputstring)) | df_batsman.ix[:,"batsman"].str.contains(str(inputstring1))]
```


### Analysis 2.1 : Comparison by Runs
#### Sample Code to integrate the runs by the Batsman
```python
df_players_comparison_by_runs = df_player_comparison.groupby(['season', 'batting_team', 'batsman'])['batsman_runs'].sum().reset_index()
df_players_comparison_by_runs.head(10)
```
<img width="674" alt="comparison_by runs" src="https://cloud.githubusercontent.com/assets/25045817/25307237/6685c32a-276b-11e7-8a68-58b7cf8d3d99.PNG">

### Conclusion
##### ~  In 2008 and 2009, MS Dhoni has scored more runs than V Kohli
##### ~ From 2010, V Kohli has improved the performance and scored more than MS Dhoni.

### Analysis 2.2 : Comparison by Balls Faced
#### Sample Code to integrate the balls faced by the Batsman
```python
df_players_comparison_by_balls_faced = df_player_comparison.groupby(['season', 'batting_team', 'batsman'])['balls_faced'].sum().reset_index()
df_players_comparison_by_balls_faced(10)
```
<img width="675" alt="comparison_by_balls_faced" src="https://cloud.githubusercontent.com/assets/25045817/25307255/af7f294a-276b-11e7-9d89-f488de2bea17.PNG">

### Conclusion
##### ~ MS Dhoni, nearly faced same number of balls in every season
##### ~ The number of balls faced by V Kohli increased over the seasons and in 2016, he has faced most balls.

### Analysis 2.3 : Comparison by Strike Rate
#### Sample Code to integrate the Strike Rate by the Batsman
```python
df_players_comparison_by_strike_rate = df_player_comparison.groupby(['season', 'batting_team', 'batsman'])['Strike-Rate'].mean().reset_index()
df_players_comparison_by_strike_rate.head()
```
<img width="624" alt="comparison_by_strikerate" src="https://cloud.githubusercontent.com/assets/25045817/25307260/cfeee1a2-276b-11e7-83cb-71aa53e2219d.PNG">

### Conclusion
##### ~ Strike rate by MS Dhoni has nearly been more than V Kohli.
