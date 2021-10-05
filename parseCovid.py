import json
import csv

#Importing or Loading from JSON File
with open('covid_cases.json','r') as json_file:
    covidjson = json.load(json_file)

#Setting the Data and Creating CSV File
covid_data = covidjson['records']
output_file = open('covid_cases.csv', 'w')
csvwriter = csv.writer(output_file)
counter = 0

#Transferring to CSV
for x in covid_data:
    if counter == 0:
        header = x.keys()
        csvwriter.writerow(header)
        counter+=1
    csvwriter.writerow(x.values())
output_file.close()