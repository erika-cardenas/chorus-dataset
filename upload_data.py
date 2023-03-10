import weaviate
import pandas as pd
import csv
import math
import numpy as np

client = weaviate.Client("http://localhost:8080")

data = pd.read_csv('data.csv')

for row in data.iterrows():
    data_properties = {}
    for key in row[1].keys():
        if key == "price":
            if not math.isnan(row[1][key]):
                data_properties[key] = int(row[1][key])
        elif key == "short_description":
            if isinstance(row[1][key], str) and not row[1][key] == "":
                data_properties[key] = row[1][key]
        else:
            data_properties[key] = row[1][key]    
    try:
        client.data_object.create(
            data_object = data_properties,
            class_name = "Products"
        )
    except:
        print(data_properties)


print("Data has been uploaded")