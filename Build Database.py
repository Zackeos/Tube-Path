import sqlite3
import csv
import os
import json

def readCSV(name):
    with open(f"./Data/{name}.csv") as file:
        csv_data = csv.reader(file, delimiter=",")
        lines = 0
        rows = []
        for row in csv_data:
            if lines == 0:
                column_titles = row
                lines += 1
            else:
                rows.append(row)
                lines += 1
    return {"titles": column_titles, "data": rows}



with open('output.json', 'w') as outfile:
    json.dump(readCSV("stations"), outfile)
