import requests
import pandas as pd
#specify the url we want to scrape from
request_url='https://en.wikipedia.org/wiki/The_World%27s_Billionaires'

#convert the link into text
site_repsonse=requests.get(request_url).text


#import BautifulSoup library to pull data out of HTML and XML files

from bs4 import BeautifulSoup
soup_content=BeautifulSoup(site_repsonse , 'html.parser')


#Fetch all the table tags
all_table=soup_content.find_all('table')



#fetch all the table tags with class name="wikitable sortable"
our_table = soup_content.find('table', class_= 'wikitable sortable')



# Defining of the dataframe

df = pd.DataFrame(columns=['No', 'Name', 'Net worth', 'Age', 'Nationality', 'Primary source(s) of wealth'])

# Collecting row data
for row in our_table.tbody.find_all('tr'):    
    # Find all data for each column
    columns = row.find_all('td')
    if(columns != []):
        no = columns[0].text.strip()
        name=columns[1].text.strip()
        net_worth=columns[2].text.strip()
        age=columns[3].text.strip()
        nationality=columns[4].text.strip()
        primary_source=columns[5].text.strip()
        df = df.append({'No': no,'Name':name,'Net worth':net_worth, 'Age':age, 'Nationality':nationality, 'Primary source(s) of wealth':primary_source},ignore_index=True)
# print(df)


#Db connections library
import psycopg2

#connection creation
connection = psycopg2.connect("dbname=webscrapper user=webscrap host=192.168.255.23 password=Bala$$90 port=5432")
cursor = connection.cursor()
#inserting rows into tables
for i,row in df.iterrows():
    sql = "INSERT INTO wiki_billionaires  VALUES (" + "%s,"*(len(row)-1) + "%s)"
    cursor.execute(sql, tuple(row))
connection.commit()

# verify the inserted rows in a table
sql = "SELECT * FROM wiki_billionaires;"
cursor.execute(sql)

# Fetch all the records and display
result = cursor.fetchall()
for i in result:
    print(i)
