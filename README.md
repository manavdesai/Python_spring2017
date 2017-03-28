# desai_manav_spring2017
Assignment 2 Comments:</br>
->Good work </br>
->Just a small error in writing the restaurant data to csv(restaurant name)</br>
Assignment 1 Comments:
->Please do not print all text in a list!!
->only 26 characters
->Q4-Check frequency value of all age group. Tried running the code you had. Threw an error
->Q6-If you initialize a list for example, after printing o/p dont  delete initialization.Code does not run
------------------------------------------------------------------------------------------------------------------------
# Midterms 

### Question_1_Analysis_1

Problem : Find out top 10 domains with highest outgoing traffic.
Procedure : Scanned through sent box of every user and selected the recipients of those emails. After that, filtering the domain names after '@' in the recipient's email address, added the count corresponding to it. Sorted the data and picked up the top 10 from them. The graph represents top 10 domains which recieved emails from given set of enron users. Finally the data is saved into a csv file.
-------------------------------------------------------------------
### Question_1_Analysis_2
Problem : Find e-mails relevant to Enron's business when Jeffrey Skilling was a CEO
Procedure : Used a set of words as a matching filter by comparing and wrote the results into a csv file
-------------------------------------------------------------------
### Question_1_Analysis_3
Problem : Find out the peak time for most of the mails sent by chairman Ken Lay

Procedure: Checking the number of emails sent by Ken Lay. Analyzing the time of the day and the number of emails sent by Ken Lay on corresponding hour of the day. Generating csv file which contains this detail. We can observe that the highest number of mails sent by him was after the office hours. 
-------------------------------------------------------------------
### Question_2_Analysis_1
Problem :  Create folder structure on the basis of section name and Find out the most published topic in the Article for the year 2010
Procedure : The data for article is not easy to retrieve directly. In order to overcome this, I initially created folder structure and saved all the files in different folders. This folder structure is based on the section name that is present in every article file. Further analysis includes the occurance of highest number of topics that were trending for the year 2010.

-------------------------------------------------------------------
### Question_2_Analysis_2
Problem : Which were the popular words used in the year
Procedure : Article Search is the data used.Traversing through list and dictionary to get section snippet. Removing all the stop words using 'NLTK' Libraries. Got frequency of all the words present in the List. Taking Word and its count in .csv file 

-------------------------------------------------------------------
### Question_2_Analysis_3
Problem: Finding the posts related to Obama
Procedure: Article Search is the data used. Traversing through list and dictionary to get section name , snippet and headlines is the initial step. Printing the details with date and number of post on Barack Obama on that particular day along with section name , snippet and headlines.
