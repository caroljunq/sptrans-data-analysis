from neo4j import GraphDatabase

# authentication
driver = GraphDatabase.driver("bolt://localhost:7687", auth=("neo4j", "123456789"))

# open session
with driver.session() as session:
    session.run("""
        CREATE (person1:Person {name: 'Eita1', age: 21})
        CREATE (person2: Person {name: 'Eita2', age: 24})
        CREATE (person1)-[:KNOWS]->(person2)
    """)
    results = session.run("MATCH (p:Person)-[:KNOWS]->(p2:Person) RETURN p")
    for result in results:
        print(result['p']['name'])
        print(result['p']['age'])

# graph.run("MATCH (p:Person) RETURN p").data()
