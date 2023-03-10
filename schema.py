import weaviate
import json

client = weaviate.Client("http://localhost:8080")

class_obj = {
   "classes": [
       {
           "class": "Products",
           "description": "Product in the chorus dataset",
           "invertedIndexConfig": {
                "indexNullState": True, # allow for null values 
        },
           "properties": [
               {
                   "name": "title",
                   "dataType": ["text"],
                   "description": "Title of the product",
               },
               {
                "name": "short_description",
                "dataType": ["text"],
                "description": "Short description of the product",
               },
               {
                   "name": "price",
                   "dataType": ["number"],
                   "description": "Price of the product",
               }
           ]
       }
   ]
}


# resetting the schema 
client.schema.delete_all()

# add the schema
client.schema.create(class_obj)

# get the schema
schema = client.schema.get()

print("Schema has been defined.")