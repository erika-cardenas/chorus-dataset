import weaviate

client = weaviate.Client("http://localhost:8080")

# Optionally set the consistency level
client.batch.consistency_level = weaviate.data.replication.ConsistencyLevel.ALL  # default QUORUM
result = client.batch.delete_objects(
    class_name="Products",
    # same where operator as in the GraphQL API
    where={
        "operator": "Equal",
        "path": ["name"],
        "valueText": "*"
    },
    output="verbose",
    dry_run=False
)

print(result)
