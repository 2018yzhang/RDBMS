import mysql.connector
import sys
import csv

searchStr = sys.argv[2]


searchStr = searchStr.replace('"', '').strip()
searchStr = searchStr.split()

cnx = mysql.connector.connect(user='inf551', password='inf551', host='127.0.0.1', database='inf551')

cursor = cnx.cursor()

query = "select distinct App, Count(Review), Avg(Sentiment_Polarity) from googleplaystore_user_reviews where Match(Review) AGAINST(%(searchT)s) group by App having Avg(Sentiment_Polarity)>0.8 and Avg(Sentiment_Subjectivity)>0.8 order by Avg(Sentiment_Polarity) DESC limit 10"

st = searchStr[0]
for x in range(1, len(searchStr)):
    st = st + ', ' + searchStr[x]


cursor.execute(query, {'searchT': st})
data = cursor.fetchall()

with open('Yidan_Zhang_q2.csv', mode='w') as csv_file:
    writer = csv.writer(csv_file)
    fieldnames = ['App', 'Reviews', 'Sentiment_Polarity']
    writer.writerow(fieldnames)
    for row in data:
            writer.writerow(row)

    
cursor.close()
cnx.close()

