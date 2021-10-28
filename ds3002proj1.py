# load cvs module 
import csv
# load json
import json
import os.path

# Operation 1: Fetch / download / retrieve a remote data file by ingesting a local file
# open file for reading 
url = 'world-happiness-report-2019.csv'
if os.path.exists(url) == False:
    print("CSV file path does not exist.")
else:
    with open(url) as csvDataFile:
    # read file as csv file 
        csvReader = csv.reader(csvDataFile)
        # Source: https://stackoverflow.com/questions/11310248/find-number-of-columns-in-csv-file
        ncol = len(next(csvReader)) # Read first line and count columns


# Operation 2: Convert the general format and data structure of the data source (from CSV to JSON)

# Create list to store all elements from the csv
data = []
# JSON file saved locally 
jsonFile = r'Happiness.json'  
rowCount = 0
if os.path.exists(url) == False:
    print("JSON file path does not exist.")
# read the csv file 
with open(url) as original:
    # Create an object that operates like a regular reader but maps the information in each row to a dict whose keys are given by the optional fieldnames parameter.
    # Source: https://docs.python.org/3/library/csv.html
    csvReader = csv.DictReader(original)
    # add each dict element to the list 
    for row in csvReader:
        data.append(row)
        rowCount = rowCount + 1
    # Convert python list to JSON 
with open(jsonFile, 'w', encoding='utf-8') as json_file:
    json_file.write(json.dumps(data, indent=5))

print("This is a brief summary of the data file ingestion:")
print("The number of rows in this file is: " + str(rowCount))
print("The number of columns in this file is: " + str(ncol))
  

