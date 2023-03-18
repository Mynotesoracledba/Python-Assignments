import requests
#specify the url we want to scrape from
request_url='https://en.wikipedia.org/wiki/The_World%27s_Billionaires'
#convert the link into text
site_repsonse=requests.get(request_url).text

# print(site_repsonse)

#import BautifulSoup library to pull data out of HTML and XML files

from bs4 import BeautifulSoup
soup_content=BeautifulSoup(site_repsonse , 'html.parser')

# #make the indentation proper
# print(soup_content.prettify())


#Fetch all the table tags
all_table=soup_content.find_all('table')
# print(all_table)

#fetch all the table tags with class name="wikitable sortable"
our_table = soup_content.find('table', class_= 'wikitable sortable')
# print(our_table)


# #In the table that we will fetch find the <a> </a>tags  
table_links = our_table.find_all('a')
# print(table_links)

# #put the title into a list 
billionaires = []
for links in table_links:
    billionaires.append(links.get('title'))
# print(billionaires)

#Convert the list into a dataframe 
import pandas as pd
df = pd.DataFrame(billionaires)
# print(df)


#To save the data into an excel file 
writer = pd.ExcelWriter('World_billionaires.xlsx', engine='xlsxwriter')
df.to_excel(writer, sheet_name='List')
writer.save()