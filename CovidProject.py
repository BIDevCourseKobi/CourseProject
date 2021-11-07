from bs4 import BeautifulSoup
import pandas as pd
import requests
import pyodbc
from sqlalchemy import create_engine
import urllib
import re
import numpy as np

"""The Worldometer URL for corona updates"""
URL = "https://www.worldometers.info/coronavirus/"

print("Getting page info...")

# sending a GET request for the URL
page = requests.get(URL)

# parsing into the html source code using beautiful soup
soup = BeautifulSoup(page.content, 'html.parser')

print("Scraping page data...")
"""---------------------------------------------TABLE---------------------------------------------"""
# extracting the html of table of data using soup
table = soup.find(id='main_table_countries_today')

"""---------------------------------------------TABLE HEAD---------------------------------------------"""
# Getting the table head HTML
thead = table.find('thead')

# getting the html columns from the table head
thead_cols = thead.find_all('th')

# List for storing the table header titles
head = []

# iterating head columns to store seach value in list
for col in thead_cols:
    head.append(col.text)

"""---------------------------------------------TABLE BODY---------------------------------------------"""
# Getting the table body HTML from table
tbody = soup.find('tbody')

# Getting all the rows in the table body
rows = tbody.find_all('tr')

# list for storing data of each row
row_data = []

# iterating each row to extract data
for row in rows:
    # extracting each column from rows
    cols = row.find_all('td')

    # extracting the text of each column and saving into a list row_data
    row = [i.text.strip() for i in cols]
    row_data.append(row)

# Lists for storing each colums
CountryID = []
Country = []
TotalCases = []
NewCases = []
TotalDeaths = []
NewDeaths = []
TotalRecovered = []
NewRecovered = []
ActiveCases = []
SeriousCritical = []
TotCases1Mpop = []
TotDeaths1Mpop = []
TotalTests = []
Tests1MPop = []
Population = []

# Iterating each row data and adding to the column lists
for row in row_data:
    CountryID.append(row[0])
    Country.append(row[1])
    TotalCases.append(row[2])
    NewCases.append(row[3])
    TotalDeaths.append(row[4])
    NewDeaths.append(row[5])
    TotalRecovered.append(row[6])
    NewRecovered.append(row[7])
    ActiveCases.append(row[8])
    SeriousCritical.append(row[9])
    TotCases1Mpop.append(row[10])
    TotDeaths1Mpop.append(row[11])
    TotalTests.append(row[12])
    Tests1MPop.append(row[13])
    Population.append(row[14])

"""---------------------------------------------EXTRACTED DATA TABULATION---------------------------------------------"""
print("Exporting scraped data...")
# creating a dataframe with each columnlist
df = pd.DataFrame({'Country ID': CountryID, 'Country': Country, 'Total Cases': TotalCases, 'New Cases': NewCases,
                   'Total Death': TotalDeaths, 'New Deaths': NewDeaths, 'Total Recovered': TotalRecovered,
                   'New Recovered': NewRecovered,
                   'Active Cases': ActiveCases, 'Serious/Critical': SeriousCritical, 'Tot Cases/ 1M pop': TotCases1Mpop,
                   'Tot Deaths/ 1M pop': TotDeaths1Mpop, 'Total Tests': TotalTests, 'Tot Tests/ 1M pop': Tests1MPop,
                   'Population': Population})
df = df.iloc[8:]

# convetring values to int and removes plus signs
for column in df:
    if column != 'Country ID' and column != 'Country':
        # removing each char other than number from cell
        df[column] = df[column].str.replace(r'[^0-9]+', '')
        # replace field that's entirely space (or empty) with NaN
        df = df.replace(r'^\s*$', np.nan, regex=True)
        # replacing nan with 0
        df[column] = df[column].fillna(0)
        # convert the column to int
        df[column] = df[column].astype(int)

# create set of parameters from connection (server, db name)
quoted = urllib.parse.quote_plus("DRIVER={SQL Server};SERVER=DESKTOP-0H19J77;DATABASE=Covid_19")
# creates sql engine
engine = create_engine('mssql+pyodbc:///?odbc_connect={}'.format(quoted))
# insert df to sql server db (fact)
df.to_sql('Fact_Corona_Updated', schema='dbo', con=engine, index=False, if_exists='replace')
# creates smaller df from dim countries
df_countries = df[['Country ID', 'Country']].drop_duplicates()
# insert dim countries to sql server db
df_countries.to_sql('Dim_Countries', schema='dbo', con=engine, chunksize=200, method='multi', index=False,
                    if_exists='replace')