# Covid-19 Project

This is the final BI Developer course project, it contains the following items:
* Covid19_project_Kobi.pbix - Power BI file with the final dashboards
* CovidProject.py - Python file with the ETL process

## Data Sources
For the project I used 3 different sources:

[The Worldometer URL for corona updates - Scrapper](https://www.worldometers.info/coronavirus/)

[csse_covid_19_data - GitHub](https://github.com/CSSEGISandData/COVID-19/tree/master/csse_covid_19_data/csse_covid_19_daily_reports)

[Our World in Data (owid-covid-data.csv) - GitHub](https://github.com/owid/covid-19-data/tree/master/public/data)

## Technologies
For the project I used the following technologies:

1. Microsoft Power BI
2. Microsoft SQL Server Management Studio
3. Pycharm and Jupyter notebook
4. Task Scheduler


## Database
I created 'Covid_19' Database with the following tables and Views:

![image](https://user-images.githubusercontent.com/93876043/141199802-eb4303ba-5339-418e-af07-7f9cd56817fd.png)

For the tables creation I used a Python code to pull the data from the web with the following libraries:

![image](https://user-images.githubusercontent.com/93876043/141200304-d53089f3-4ef4-4dfe-9342-187e12a70756.png)

For pulling the data from a webpage I used a 'BeatifulSoup' library that works well with web data and also used 'requestes' and 'urllib' to connect to the data, then I transferred the data to a dataframe using Pandas library.

For other ETL processes I used regular expressions 're'/ 'Numpy'/'Pandas' libraries to remove some unwanted characters from some columns and replace nulls with zeros and finally convert the types of some columns to integers.

With sqlalchemy library I created and inserted dataframes to my 'Covid_19' DB, this is the code for the first df I inserted:

![image](https://user-images.githubusercontent.com/93876043/141815032-2153d9c4-456c-42b2-a4d0-6a9474986275.png)

And finally I user SQL server management studio to create a view that takes the latest data from the table '[Fact_Corona_Updated_source3] with the grouped data by country from the table '[Fact_Corona_Updated_source2]' and present the total confirmed cases and the new cases.

![image](https://user-images.githubusercontent.com/93876043/141202941-87206fcc-b3ad-4b1a-a29e-6001babec3c1.png)

## Schedule
To schedule the data I used the windows 10 Task Scheduler to run daily the 'CovidProject.py' file

![image](https://user-images.githubusercontent.com/93876043/141815267-63f50b49-d03d-4ed9-b8d5-396471cc402f.png)

I created a new action to run the Python script

![image](https://user-images.githubusercontent.com/93876043/141819832-8fa9edcb-de99-4c7b-8d57-2a10cc4d0e85.png)

And added a trigger to run the file daily at 9:00AM (GMT+2)

![image](https://user-images.githubusercontent.com/93876043/141204107-f2fecd6d-7faf-4e8c-8694-0832919e109e.png)

## Dashboards
I created 3 dashboards:

* Web
* DWH
* Vaccinations

### Web

The data from [The Worldometer URL for corona updates](https://www.worldometers.info/coronavirus/) that show today's worldly covid data, for this I used Power BI to import the data from a web page (Yesterday's Data) and all the ETL was done in Power Query.

![image](https://user-images.githubusercontent.com/93876043/141204630-032d0f51-1363-4c3d-8348-9b1c8c5b7842.png)

### DWH

Same data as on previous dashboard (Except this data is from 'Now' table) but this time the data arrived after the full ETL process that was mentioned before, the data was imported from a SQL database.

### Vaccinations

Here we see the combined covid data from the other tables/sources + view

![image](https://user-images.githubusercontent.com/93876043/141205612-ac231f36-e791-4ff0-bab5-a6d905db37f5.png)


Thank you!






