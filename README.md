# Covid-19 Project

This is the final BI Developer course project, it contains the following items:
* Covid19_project_Kobi.pbix - Power BI file with the final dashboards
* CovidProject.py - Python file with the ETL process

## Data Sources
For the project I used 3 different sources:

[The Worldometer URL for corona updates](https://www.worldometers.info/coronavirus/)

[csse_covid_19_data](https://github.com/CSSEGISandData/COVID-19/tree/master/csse_covid_19_data/csse_covid_19_daily_reports)

[Our World in Data (owid-covid-data.csv)](https://github.com/owid/covid-19-data/tree/master/public/data)

## Softwares/IDE
For the project I used the following softwares:

1. Microsoft Power BI
2. Microsoft SQL Server Management Studio
3. Pycharm and Jupyter notebook


## Database
I created 'Covid_19' Database with the following tables and Views:

![image](https://user-images.githubusercontent.com/93876043/141199802-eb4303ba-5339-418e-af07-7f9cd56817fd.png)

For the tables creation I used a Python code to pull the data from the web with the following libraries:

![image](https://user-images.githubusercontent.com/93876043/141200304-d53089f3-4ef4-4dfe-9342-187e12a70756.png)

For pulling the data from a webpage I used a 'BeatifulSoup' library that works well with web data and also used 'requestes' and 'urllib' to connect to the data, then I transferred the data to a dataframe using Pandas library.

For other ETL processes I used regular expressions 're'/ 'Numpy'/'Pandas' libraries to remove some unwanted characters from some columns and replace nulls with zeros and finally convert the types of some columns to integers.

With sqlalchemy library I created and inserted dataframes to my 'Covid_19' DB, this is the code for the first df I inserted:

![image](https://user-images.githubusercontent.com/93876043/141200827-0a6e3ae7-1694-4422-a74d-c8e2ad769ce7.png)

And finally I user SQL server management studio to create a view that takes the latest data from the table '[Fact_Corona_Updated_source3] the data from the tables

![image](https://user-images.githubusercontent.com/93876043/141202941-87206fcc-b3ad-4b1a-a29e-6001babec3c1.png)





