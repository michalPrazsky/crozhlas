import pandas as pd
import os
import json
import datetime
import matplotlib.pyplot as plt

directory = "./target"

dataset = []

for root, dirs, files in os.walk(directory):
    for file in files:
        if file.endswith(".json"):
            path = os.path.join(root,file)  

            with open(path) as file:
                data = json.load(file)
                del data["count"]
                del data["status"]

                date = data["date"]
                del data["date"]

                year, month, day = map(int, date.split("-"))
                no_week = datetime.date(year, month, day).isocalendar()[1]
                
                data["week-number"] = no_week
                data["year"] = year
                dataset.append(data)

df = pd.DataFrame(dataset) 

df.to_excel("output.xlsx", index=True)
print(df)

