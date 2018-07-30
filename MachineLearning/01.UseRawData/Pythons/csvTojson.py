import csv
import json
import os, os.path

#Read csv RawData
def convert_csvTojson(rawDataPath, csvFile):
    with open(rawDataPath + csvFile, 'r') as csvMemory:
        reader = csv.DictReader(csvMemory)
        rows = list(reader)

    with open(rawDataPath + '\Data.json', 'w') as jsonMemory:
        json.dump(rows, jsonMemory, indent=2)


csvFileName = '\Data.csv'
rawDataPath = '..\RawData'

if os.path.exists(rawDataPath + csvFileName):
    convert_csvTojson(rawDataPath, csvFileName)



