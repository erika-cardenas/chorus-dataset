# chorus-dataset
Welcome to the first demo using the Chorus dataset. (:

The four main files you want to focus on are `docker-compose.yaml`, `schema.py`, `upload_data.py`, and `query.py`. Here is a step-by-step on how to run this demo on your local computer:

## Preliminary step:
Make sure you have the Weaviate Python client installed. [Here](https://weaviate.io/developers/weaviate/client-libraries/python) is the documentation on how to do so, but here is the code:
```
$ pip install weaviate-client
```

## Step 1: 
To run Weaviate locally, we need to run our yaml file. For simplicity, we are using the [`text2vec-transformers`](https://weaviate.io/developers/weaviate/modules/retriever-vectorizer-modules/text2vec-transformers).
We can eventually switch this to use any vectorizer like OpenAI, Cohere etc. 

Run this command to get docker running;

```
docker-compose up
```

## Step 2: 
In Weaviate, you create schemas to capture each of the entities you will be searching. Our demo has three properties (`title`, `short_description`, `price`) 
that belong to the `Poducts` class. Since we have a `null` values, we want to be able to filter for objects that have empty properties. 

Run this to define the schema;

```
python3 schema.py
```

## Step 3:
Now that we have defined our schema, we will need to upload our data. Due to the null values, we had to parse our data to upload it correctly. The main parts to focus on 
are the `client.data_object.create()` parameter. We are setting the `data_object` to the properties that we defined in the schema and defining the `class_name`, which we already did in the schema. 

Run this command to upload your data;

```
python3 upload_data.py
```

## Step 4:
We can now query our data! There are two options for you to run the queries: 1. run the `query.py` file or 2. use the [console](https://console.weaviate.io/)

### Step 4.1
The `query.py` file has 4 examples that are using the python client.  

### Step 4.2
If you prefer to use the console, put `http://localhost:8080` in the Self-hosted Weaviate box. 

### Quick explanation of the queries

#### Query 1: 
As mentioned earlier, there were quite a few `null` values for `price` and `short_description`. This query allows you to see the products that have null values in price. 

#### Query 2:
This query is running pure vector search (`nearText`). It is finding concepts related to "ethernet cord". We can also see the certainty under additional.

#### Query 3:
This query is using **hybrid** search. `alpha` is a parameter used to give a weight to bm25 and vector search. With `alpha` set to 0.75, it is applying more weight to the dense vectors. 
I also added in a where filter to find pc laptops that are in between the 100 and 2000 price range. 

#### Query 4:
This query is using **bm25**. I want to find hp laptops and boost the `title` property -- hence the `"title^2"`. 
