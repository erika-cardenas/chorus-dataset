import weaviate
import pandas as pd
import math
import base64
import requests
import numpy as np
import csv
import logging
import os

client = weaviate.Client("http://localhost:8080")
# Configure the logging system
logging.basicConfig(filename='app.log', level=logging.DEBUG)
path_to_json_files = 'data/'

def read_data_files():
    #get all JSON file names as a list
    json_file_names = [
            filename for filename in os.listdir(path_to_json_files)
                if filename.endswith('.json')
        ]
    for json_file_name in json_file_names:
        with open(os.path.join(path_to_json_files, json_file_name)) as json_file:
            data = pd.read_json(json_file)
            ingest_data(data)


def ingest_data(data):
    for row in data.iterrows():
        data_properties = {}
        for key in row[1].keys():
            if key == "price":
                if not math.isnan(row[1][key]):
                    data_properties[key] = int(row[1][key])
            elif key == "short_description":
                if isinstance(row[1][key], str) and not row[1][key] == "":
                    data_properties[key] = row[1][key]
            elif key == "img_high":
                # Set the image URL
                url = row[1][key]
                # Retrieve the image data
                response = requests.get(url)
                image_data = response.content
                # Encode the image data as Base64
                base64_image = base64.b64encode(image_data).decode('utf-8')
                # Output the Base64-encoded value
                data_properties[key] = base64_image
            elif key == "title":
                data_properties[key] = row[1][key]
            elif key == "name":
                data_properties[key] = row[1][key]
            elif key == "ean":
                data_properties[key] = row[1][key]
            elif key == "date_released":
                data_properties[key] = row[1][key]
            elif key == "supplier":
                data_properties[key] = row[1][key]
            elif key == "brand":
                data_properties[key] = row[1][key]
            elif key == "product_type":
                data_properties[key] = row[1][key]
            # else:
            # this should take care of all mapped props ?
        try:
            client.data_object.create(
                data_object=data_properties,
                class_name="Products"
            )
        except BaseException as exception:
            logging.warning(f"Exception Name: {type(exception).__name__}")
            logging.warning(f"Exception Desc: {exception}")
            # print(data_properties)
        print("Data has been uploaded")

if __name__ == "__main__":
    read_data_files()