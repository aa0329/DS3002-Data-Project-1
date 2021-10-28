# DS3002-Data-Project-1

## How to use the data processor:

This data processor ingests a pre-defined data source, so no commandline arguments are needed to supply the data file. 

The data processor is ran using the commandline by entering "python3 ds3002proj1.py"

## The elements that make the data processor operational:

The first portion of the data processor imports the necessary modules needed (csv, json, os.path)
* csv: This module is used to read the csv data source to be able to complete the first benchmark
* json: This module is used to convert the general format and data structure of the data source from CSV to JSON
* os.path: This module is used to check if a file exists on the disk to generate appropriate error messages if necessary

The second portion of the data processor implements operation 1 - Fetch / download / retrieve a remote data file by ingesting a local file
1. Create a variable to store the data source
2. Create an error message if the file doesn't exist
3. Otherwise, read the file as a csv file
4. Read the first line and count the columns and save into variable to use later for operation 5

The third portion of the data processor implements operation 2 - Convert the general format and data structure of the data source (from CSV to JSON)
1. First, create a list to store all elements from the csv
2. Create a local JSON file variable
3. Create an error message if the file doesn't exist
4. Open the csv file and use DictReader to create an object that maps the information in each row to a dict whose keys are given by the optional fieldnames parameter.
5. Then, each row from the resulting operation is put into the list from Step 1 and a row counter is incremented to and saved into variable to use later for operation 5
6. Lastly, the list is converted to JSON using json.dumps

The fourth portion of the data processor implements operation 5 - Generate a brief summary of the data file ingestion including: 1. Number of records 2. Number of columns
1. This part includes print statements that prints the number of rows and columns that were calculated in steps 4 of the second portion and steps 5 of the third portion
