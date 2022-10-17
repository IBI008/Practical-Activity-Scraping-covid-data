#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Import necessary library
import requests
import pandas as pd
from bs4 import BeautifulSoup


# In[2]:


# Establish connection with URL.
# Create a url variable.
url = 'https://www.worldometers.info/coronavirus/'

# Create a requests variable.
r = requests.get(url)

# Make contact with the website.
if r.status_code == 200:
    html_doc = r.text
    
# Get a BeautifulSoup object.
soup = BeautifulSoup(html_doc)

# Print the output.
print(soup.prettify())


# In[3]:


# Extract tabular data.
# Extract the contents of the table with the table id. 
table = soup.find('table', attrs={'id': 'main_table_countries_today'})

# View the table.
table


# In[5]:


# Extract table header
# Specify BeautifulSoup to go through the table and find everything 
# with a tr tag.
# Note: th = (table header), tr = (table row), and td = table column
rows = table.find_all('tr', attrs={'style': ""})

# View the result.
rows


# In[6]:


# Store the extracted data.
output = []

column_names = ['Country,Other', 'Total Cases', 'New Cases', 'Total Deaths',
               'New Deaths', 'Total Recovered', 'New Recovered',
               'Active Cases', 'Serious, Critical', 'Tot Cases/ 1M pop',
               'Deaths/ 1M pop', 'Total Tests', 'Tests/ 1M pop', 'Population']

# Create a for loop statement.
for cases in rows:
    cases_data = cases.find_all("td")
    if cases_data:
        # Extract the text within each element.
        cases_text = [td.text for td in cases_data]
        output.append(dict(zip(column_names, cases_text)))
        
# Create an output.
output


# In[7]:


# Convert extracted data into a pandas dataframe
# Create a DataFrame directly from the output.
data = pd.DataFrame(output)

# View the DataFrame.
data.head()


# In[ ]:




