# Operation 1: Fetch / download / retrieve a remote data file by ingesting a local file

# load cvs module 
import csv

# open file for reading 
url = 'world-happiness-report-2019.csv'
with open(url) as csvDataFile:
# read file as csv file 
    csvReader = csv.reader(csvDataFile)