# Stock_Market_DataLake

historical.py -> script for historical dump

incremental.py -> script for a daily dump



cron job @01:00 -> 0 1 * * * /incremental.py



MySQL is used as a DataBase to analyse and query data



Composite Indexing of table is done on date, company

This index will ensure efficient filtering and grouping of the data, resulting in improved query performance