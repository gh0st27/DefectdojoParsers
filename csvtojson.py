import csv 
import json
import pandas as pd

def csv_to_json(csvFilePath, jsonFilePath):
    jsonArray = []
    
      
    #read csv file
    with open(csvFilePath, encoding='utf-8-sig') as csvf: 
        #load csv file data using csv library's dictionary reader
        csvReader = csv.DictReader(csvf) 

        #convert each csv row into python dict
        for row in csvReader: 
            #add this python dict to json array
            jsonArray.append(row)
    
    nested_dict = {"findings": jsonArray }
    #print(nested_dict)
    #convert python jsonArray to JSON String and write to file
    with open(jsonFilePath, 'w', encoding='utf-8-sig') as jsonf: 
        jsonString = json.dumps(nested_dict, indent=4)
        jsonf.write(jsonString)
        
def csv_conversion(rawCSVFile):
    aa = pd.read_csv(rawCSVFile)
    aa['severity'] = 'High'
    aa['active'] = aa.loc[:, 'Status']
    aa['active'] = aa['active'].replace(['Open', 'Closed', 'Exception'], ['True', 'False', 'True'])
    aa.rename(columns = {'Security Requirement':'title'}, inplace = True)
    aa.rename(columns = {'Source Name':'file_path'}, inplace = True)
    aa.rename(columns = {'Source':'references'}, inplace = True)
    aa.rename(columns = {'Status':'mitigation'}, inplace = True)
    aa.rename(columns = {'Description':'description'}, inplace = True)
    aa.to_csv('requirements.csv', index=False) 
    
rawCSVFile = 'raw.csv'          
csvFilePath = r'requirements.csv'
jsonFilePath = r'requirements.json'

csv_conversion(rawCSVFile)
csv_to_json(csvFilePath, jsonFilePath)

#Note - title,	file_path,	references,	active,	mitigation,	severity,	description must be in lowercase
#Note - Open, closed, Exception issue should be marked True, False and True respectively 
#Note - severity column must be added
