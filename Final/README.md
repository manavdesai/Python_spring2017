<img width="550" alt="bat"
src="https://cloud.githubusercontent.com/assets/25045817/25302244/09900832-2708-11e7-9585-279805797ce8.png">

# Indian Premier League - OPEN DATA ANALYSIS
## Content 
* Introduction
* Analysis-1 : Analysis on batsmen
* Analysis-2 : Comparison of Players
* Analysis-3 : Analysis on bowlers
* Analysis-4 : Team-based analysis
* Analysis-5 : Toss-based analysis
## Introduction

The Indian Premier League (IPL) is a professional Twenty20 cricket league in India contested during April and May of every year by teams representing Indian cities. There are different teams with different players from different countries playing against each other to win IPL cup. The dataset represents information on different players, their performance, wickets and victory.

Using the dataset of this cricket league, I have performed analysis and asnwered various questions that may be helpful in future for the prediction or to determine the consistency of a player, team or a match. 

This data contains the facts across all 8 seasons (2008 - 2016) and all the analysis are for the records over the season.

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
## Analysis-1 : Analysis on batsmen <img width="206" alt="bat" align="right" src="https://cloud.githubusercontent.com/assets/25045817/25307524/48f3c6e0-2770-11e7-8d96-3a17c55e7748.PNG">

In this analysis, I have integrated the facts related to a batsman and how it relates to his performance. Considering the number of runs scored by the batsman, his performance has been tracked over the years. The number of FOURS and SIXES hit by a batsman is analyzed and also to consider the number of dot balls given by batsman.
### Analysis 1.1 : Top Run scorers
Using deliveries.csv, integrated all the runs by the batsmen and displayed top 10 of them. 
#### Code
```python
runs_df = df_deliveries.groupby('batsman')['batsman_runs'].agg('sum').reset_index().sort_values(by='batsman_runs', ascending=False).reset_index(drop=True)
runs_df = runs_df.iloc[:10,:]

```
<img width="582" alt="top_run_scorers" src="https://cloud.githubusercontent.com/assets/25045817/25302728/e84f1cd4-2712-11e7-8e33-2a9f5b865448.PNG">

### Conclusion
##### ~ V Kohli is the top run scorer amongst all followed by SK Raina.
##### ~ CH Gayle and DA Warner are highest run scorers in foreign players.
************************************************************************************************************************************
### Analysis 1.2 : Performance of Top 5 Batsmen 
using batsman dataframe created above, displayed the performance of batsmen over all the years.
#### Code
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
### Analysis 1.3 : Batsmen who have hit maximum number of FOURS 
using deliveries.csv, grouped the batsmen data by the number of FOURS hit by them and sorted in descending order.
#### Code
```python
fours_df = df_deliveries.groupby('batsman')['batsman_runs'].agg(lambda x: (x==4).sum()).reset_index().sort_values(by='batsman_runs', ascending=False).reset_index(drop=True)
fours_df = fours_df.iloc[:10,:]
fours_df.head()

```
<img width="507" alt="players_with_4s" src="https://cloud.githubusercontent.com/assets/25045817/25302971/4eef6962-2718-11e7-826a-f2b8f4accc4e.PNG">

### Conclusion 
##### ~  G Gambhir has hit maximum number of FOURS. Total of 422 Fours
************************************************************************************************************************************
### Analysis 1.4 : Batsmen who have hit maximum number of SIXES 
using deliveries.csv, grouped the batsmen data by the number of SIXES hit by them and sorted in descending order.
#### Code
```python
six_df = df_deliveries.groupby('batsman')['batsman_runs'].agg(lambda x: (x==6).sum()).reset_index().sort_values(by='batsman_runs', ascending=False).reset_index(drop=True)
six_df = six_df.iloc[:10,:]
six_df.head()

```
<img width="498" alt="players_with_6s" src="https://cloud.githubusercontent.com/assets/25045817/25303101/0bb24c94-271a-11e7-865e-72490cb8fc14.PNG">

### Conclusion 
##### ~ CH Gayle has hit maximum number of SIXES. Total 252 Sixes. 
************************************************************************************************************************************
### Analysis 1.5 : Batsmen who played maximum number of Dot balls
using deliveries.csv, grouped the batsmen data by the number of DOT balls played by them and sorted in descending order.
####  Code
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
## Analysis-2 : Comparison of players

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
#### Code to integrate the runs by the Batsman
```python
df_players_comparison_by_runs = df_player_comparison.groupby(['season', 'batting_team', 'batsman'])['batsman_runs'].sum().reset_index()
df_players_comparison_by_runs.head(10)
```
<img width="674" alt="comparison_by runs" src="https://cloud.githubusercontent.com/assets/25045817/25307237/6685c32a-276b-11e7-8a68-58b7cf8d3d99.PNG">

### Conclusion
##### ~  In 2008 and 2009, MS Dhoni has scored more runs than V Kohli
##### ~ From 2010, V Kohli has improved the performance and scored more than MS Dhoni.

### Analysis 2.2 : Comparison by Balls Faced
#### Code to integrate the balls faced by the Batsman
```python
df_players_comparison_by_balls_faced = df_player_comparison.groupby(['season', 'batting_team', 'batsman'])['balls_faced'].sum().reset_index()
df_players_comparison_by_balls_faced(10)
```
<img width="675" alt="comparison_by_balls_faced" src="https://cloud.githubusercontent.com/assets/25045817/25307255/af7f294a-276b-11e7-9d89-f488de2bea17.PNG">

### Conclusion
##### ~ MS Dhoni, nearly faced same number of balls in every season
##### ~ The number of balls faced by V Kohli increased over the seasons and in 2016, he has faced most balls.

### Analysis 2.3 : Comparison by Strike Rate
#### Code to integrate the Strike Rate by the Batsman
```python
df_players_comparison_by_strike_rate = df_player_comparison.groupby(['season', 'batting_team', 'batsman'])['Strike-Rate'].mean().reset_index()
df_players_comparison_by_strike_rate.head()
```
<img width="624" alt="comparison_by_strikerate" src="https://cloud.githubusercontent.com/assets/25045817/25307260/cfeee1a2-276b-11e7-83cb-71aa53e2219d.PNG">

### Conclusion
##### ~ Strike rate by MS Dhoni has nearly been more than V Kohli.

***************************************************************************************************************************************
***************************************************************************************************************************************
## Analysis-3 : Analysis on Bowlers <img width="177" alt="bowlerds" align="right" src="https://cloud.githubusercontent.com/assets/25045817/25307387/2ef02e20-276e-11e7-8f78-b2587161ea6d.PNG">

Bowlers play an important role in cricket. While batsman are for scoring against opponent team, Bowlers are for dismissing players in the opponent team
In this analysis, I have presented the performances of the bowlers and given the statistical data about the wickets taken, the average economy by them, reasons for the wicket and also the extras that they have given over the seasons. This analysis is helpful if we want to make a decision about selecting the right candidate for bowling according to the scenarios. 

### Analysis 3.1 : Highest Wicket Takers 
#### Code to integrate the wicket data by bowlers
```python
wicket_kinds = ["bowled", "caught", "lbw", "stumped", "caught and bowled", "hit wicket"] 
check=df_deliveries[df_deliveries["dismissal_kind"].isin(wicket_kinds)]
```
<img width="531" alt="highest_wicket_takers" src="https://cloud.githubusercontent.com/assets/25045817/25307460/49a72cf4-276f-11e7-955a-70462c25c658.PNG">

### Conclusion <img width="215" alt="malinga" align="right" src="https://cloud.githubusercontent.com/assets/25045817/25307476/8a0340ee-276f-11e7-8876-5e35833cb799.PNG">

##### ~ SL Malinga and DJ Bravo are 2 foreign bowlers with highest Wicket takers
##### ~ A Mishra and PP Chawla are 2 Indian bowlers with highest Wicket takers
##### ~ DW Steyne and Z Khan have taken equal number of wickets

### Analysis 3.2 : Analysis by Economy over the season
#### Code to integrate the wicket data by bowlers
```python
df_over=df_deliveries.groupby(['bowler']).sum()
df_over['total balls']=df_deliveries['bowler'].value_counts()
df_over['overs']=(df_over['total balls']//6) # because each over has 6 balls
df_over[df_over['overs']>200].sort_values(by='overs',ascending=0)[[14]].head(5).T
df_over['economy']=(df_over['total_runs']/(df_over['overs']))
df_over[(df_over['overs']>300)].sort_values('economy')[:10].economy.reset_index().T
```
<img width="519" alt="average_economy" src="https://cloud.githubusercontent.com/assets/25045817/25307554/c072385a-2770-11e7-873f-702ebfd16cdf.PNG">

### Conclusion
##### ~ The average economy rate is between 8.5 - 9

### Analysis 3.3 : Reasons for wicket <img width="158" alt="reasons_for_wickets" align="right"  src="https://cloud.githubusercontent.com/assets/25045817/25307590/9e9991f0-2771-11e7-8652-0be41c3d4793.png">
#### Code to integrate the wicket data by bowlers
```python
wicket=["run out","bowled", "caught", "lbw", "stumped", "caught and bowled", "hit wicket"]
check=df_deliveries[df_deliveries["dismissal_kind"].isin(wicket)]
top=check.dismissal_kind.value_counts()[:10].plot.bar(width=0.7,color='#58D68D')
for each in top.patches:
    top.annotate(format(each.get_height()), (each.get_x()+0.1, each.get_height()+1))
```
<img width="508" alt="reasons_for_wickets" src="https://cloud.githubusercontent.com/assets/25045817/25307565/0d91f83c-2771-11e7-8bab-5cdefecdf136.PNG">

### Conclusion
##### ~ Maximum wickets occur because of 'Catches'
##### ~ Minimum wickets occur because of 'Hit wickets'

### Analysis 3.4 : Analysis on EXTRA runs
#### Code to integrate the wicket data by bowlers
```python
extras=df_deliveries[['wide_runs','bye_runs','legbye_runs','noball_runs']].sum()
```
<img width="450" alt="percentage_of_extras" src="https://cloud.githubusercontent.com/assets/25045817/25307574/3c49ad78-2771-11e7-94d9-8167ec0cfc8a.PNG">

### Conclusion
##### ~ Wide Runs is biggest reason for EXTRAS given
##### ~ No Ball Runs is least reason for EXTRAS given

***************************************************************************************************************************************
***************************************************************************************************************************************

## Analysis-4 : Team-based Analysis <img width="400" alt="teams" align="right" src="https://cloud.githubusercontent.com/assets/25045817/25307692/30ad71b4-2773-11e7-8688-824577fd1d6b.PNG">
Batsman and bowlers work together in a team. At the end, it's the team work which is responsible for victory or defeat. 
In this analysis, I have presented the performances of the team as whole. Playing on their home grounds to different places, I have collected the information about their win in different cities. 

The analysis on teams that can handle pressure (ie.Win by less than 10 Runs or Win by less than 2 Wicket) is done which reflects their efficiency of team work in critical situations. 

Also, The analysis on teams which won by sheer dominance or by big margin is done ( ie. Win by more than 50 Runs or Win by more than 7 Wickets) which reflects how strong is the team against the losing team.

#### Sample Code to calculate the aggregate od matches
```python
df_aggregates = pd.merge(df_matches, df_all_matches_score, left_on='id', right_on= 'match_id', how='outer')
df_aggregates.head(2)

```

### Analysis 4.1 : Team wins in different cities
#### Code
```python
df_total_wins_per_city = df_aggregates[df_aggregates['season'] == 2008].groupby(['winner','city'])['match_id'].count().unstack()
df_total_wins_per_city.head(10)

```
<img width="603" alt="team_wins_in_cities" src="https://cloud.githubusercontent.com/assets/25045817/25307830/37d4a0d6-2776-11e7-802a-9998d6d27296.png">

### Conclusion
##### ~ All the teams have won the most on their Home Grounds
##### ~ Royal Challengers Bangalore doesn't seem to be affected with their Home city. They have nearly equal number of wins in every city
##### ~ Rajasthan Royals have won the most number of matches
##### ~ Deccan Chargers have won the least number of matches


### Analysis 4.2 : Teams which managed to win under pressure
#### Code
```python
df_close = df_matches[((df_matches['win_by_runs']<10) & (df_matches['win_by_runs']>0)) 
                                  | ((df_matches['win_by_wickets']<=2) & (df_matches['win_by_wickets']>0))]
df_close.head()

```
<img width="481" alt="team_wins_under_pressure" src="https://cloud.githubusercontent.com/assets/25045817/25307944/56692a7e-2778-11e7-94a2-4b6aea3c32bf.PNG">

### Conclusion
##### ~ Kings XI Punjab have handled their nerves in Pressure and won the games maximum number of times when the margin was less
##### ~ Pune Warriors, Kochi Tuskers Kerala and Gujarat Lions doesn't seem to handle pressure easily

### Analysis 4.3 : Team wins by Big Run Margin
#### Code
```python
df_big_margin = df_matches[((df_matches['win_by_runs']>=50) | (df_matches['win_by_wickets']>=7))]
df_big_margin.head(2)
df_big_margin.groupby("winner")["id"].count()
```
<img width="506" alt="team_wins_big_margin" src="https://cloud.githubusercontent.com/assets/25045817/25307975/dd638150-2778-11e7-8ac2-55a6914fa841.PNG">

### Conclusion
##### ~ Royal Challengers Bangalore and Chennai Super Kings have won the matches with sheer dominance.

***************************************************************************************************************************************
***************************************************************************************************************************************

## Analysis-5 : Toss-based Analysis <img width="100" alt="toss" align="right" src="https://cloud.githubusercontent.com/assets/25045817/25308075/1533665c-277b-11e7-90e0-f8acf33339a2.PNG">
In this analysis, I have focussed on the decisions made by team after winning the toss. A toss gives the winner a priority to decide what he wants to do first, Bat or field?
Analysis has been made on the decisions taken by the teams to bat or field first as the teams might have certain strategy of approaching the game. 
In this analysis, I have presented the facts of toss decisions over the seasons, toss winners and their count, probability of winning a toss. Also, there is a belief that TOSS winner is a MATCH winner. Let's see how true it is !

### Analysis 5.1 : Overall toss decision in percentage
#### Code
```python
print('Toss Decisions in Percentage \n')
df_toss=((df_matches['toss_decision']).value_counts())/577*100
df_toss
```
<img width="195" alt="overall_toss_decision" src="https://cloud.githubusercontent.com/assets/25045817/25308166/e3d04b8c-277c-11e7-92d2-a5148078592d.PNG">

## Conclusion
##### ~ Fielding first has been more of a preference


### Analysis 5.2 : Decision across seasons by Toss winning captains

<img width="658" alt="toss_decision_by_season" src="https://cloud.githubusercontent.com/assets/25045817/25308213/c5cd87ac-277d-11e7-8b61-00b2d7b3ec24.PNG">

## Conclusion
##### ~ The decision for batting or fielding varies largely across the seasons. 
##### ~ In 2016 though, the majority of toss winners opted to Field first, may be because they could have their targets set  and they can plan a strategy for batting.

### Analysis 5.3 : Toss Winners  
#### Code
```python
top=df_matches['toss_winner'].value_counts().plot.bar(width=0.4, color= 'Orange')
for each in top.patches:
    top.annotate(format(each.get_height()), (each.get_x()+0.15, each.get_height()+1))
```
<img width="602" alt="toss_winners_over season" src="https://cloud.githubusercontent.com/assets/25045817/25308231/109a6a7a-277e-11e7-853f-2cc23c16711c.PNG">

### Conclusion
##### ~ Mumbai Indians have the higest TOSS wins followed by Kolkata Knight Riders. 
##### ~ Pune Supergiants have the lowest wins as they have played the lowest matches also.

### Analysis 5.4 : Probability of Winning the toss 
#### Code
```python
winner=df_matches['toss_winner'].value_counts()
match=pd.concat([df_matches['team1'],df_matches['team2']]).value_counts()
top=(winner/match*100).sort_values().plot.bar(width=0.5,color='purple')
for each in top.patches:                       
    top.annotate('{:.2f}%'.format(each.get_height()), (each.get_x(), each.get_height()+1),fontsize=9)
```
<img width="600" alt="probability_of_winning_toss" src="https://cloud.githubusercontent.com/assets/25045817/25308246/5b9ad0b4-277e-11e7-9c0f-083428fb1679.PNG">

### Conclusion
##### ~ the chance for winning a toss is highest for DC (Deccan Chargers) and it is lowest for PW (Pune Warriors).


### Analysis 5.5 : Probability of TOSS winner to also be a MATCH winner 
#### Code
```python
decision=df_matches[df_matches['toss_winner']==df_matches['winner']]
slices=[len(decision),(577-len(decision))]
```
<img width="456" alt="toss_decision_and_winner" src="https://cloud.githubusercontent.com/assets/25045817/25308287/bf0d8808-277e-11e7-9033-9da9ccd97a4c.PNG">

### Conclusion:
##### ~ The match winning probablity for toss winning team is about 50%-50%
##### ~ The myth that Toss winner usually wins the match stands FALSE here
