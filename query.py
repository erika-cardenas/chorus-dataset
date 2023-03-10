import weaviate

client = weaviate.Client("http://localhost:8080")

# QUERY EXAMPLE ONE 

query_one = """
{
  Get {
    Products (
      where: {
        operator: IsNull, path: "price", valueBoolean: true}
    ) {
      price
      short_description
      title
    }
  }
}
"""

result = client.query.raw(query_one)
print(result)


# QUERY EXAMPLE TWO 

query_two = """
{
  Get {
    Products (
      nearText: {
        concepts: "ethernet cord"
      }) {
      short_description
      title
      _additional {
        certainty
      }
    }
  }
}
"""

result = client.query.raw(query_two)
print(result)


# QUERY EXAMPLE THREE

query_three = """
{
  Get {
    Products(
      hybrid: {query: "pc laptop", alpha: 0.75},
      where: {
      operator: And,
      operands: [{
          path: "price",
          operator: GreaterThan,
          valueNumber: 100
        }, {
          path: "price",
          operator: LessThan,
          valueNumber: 2000
        }]
      }) {
		price
        title
        short_description
    }
  }
}
"""

result = client.query.raw(query_three)
print(result)


# QUERY EXAMPLE FOUR

query_four = """
{
  Get {
    Products(
      bm25: 
        {query: "hp laptop", properties: ["title^2", "short_description"]}
    ){
        price
        title
        short_description
        _additional {
            score
      }
    }
  }
}
"""

result = client.query.raw(query_four)
print(result)

