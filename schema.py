import weaviate
import json

client = weaviate.Client("http://localhost:8080")

class_obj = {
    "classes": [
        {
            "class": "Products",
            "description": "Product in the chorus dataset",
            "invertedIndexConfig": {
                "indexNullState": True,  # allow for null values
            },
            "vectorIndexType": "hnsw",
            "vectorizer": "multi2vec-clip",
            "moduleConfig": {
                "multi2vec-clip": {
                    "imageFields": [
                        "img_high"
                    ],
                    "textFields": [
                        "name",
                        "title",
                        "brand"
                    ]
                    # If only a single property, the property takes all the weight.
                    # If multiple properties exist and no weights are specified, the properties are equal-weighted.
                    # "weights": {
                    #    "textFields": [0.7],
                    #    "imageFields": [0.3]
                    # }
                }
            },
            "properties": [
                # missing provision for user defined 'id' field
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
                },
                {
                    "name": "img_high",
                    "dataType": ["blob"],
                    "description": "High resolution image of the product",
                },
                {
                    "name": "name",
                    "dataType": ["text"],
                    "description": "Name of the product",
                },
                {
                    "name": "ean",
                    "dataType": ["string[]"],
                    "description": "EAN of the product",
                },
                {
                    "name": "date_released",
                    "dataType": ["date"],
                    "description": "Released Date of the product",
                },
                {
                    "name": "supplier",
                    "dataType": ["text"],
                    "description": "Supplier of the product",
                },
                {
                    "name": "brand",
                    "dataType": ["text"],
                    "description": "Brand of the product",
                },
                {
                    "name": "product_type",
                    "dataType": ["text"],
                    "description": "Type of the product",
                }
            ]
        }
    ]
}

# resetting the schema
client.schema.delete_all()

# add the schema
client.schema.create(class_obj)

# update the schema
# client.schema.update_config("Products", class_obj)

# get the schema
schema = client.schema.get()

print("Schema has been defined.")
