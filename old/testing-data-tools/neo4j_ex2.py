from py2neo import Graph, Node, Relationship
from pandas import DataFrame
# import py2neo
graph = Graph(ip_addr = 'bolt://localhost:7687', username = 'neo4j', password = '123456789')

p1 = Node("Person", name="eita1",age=22)
p2 = Node("Person", name="eita2",age=24)
p1p2 = Relationship(p1, "KNOWS", p2)
graph.create(p1)
graph.create(p2)
graph.create(p1p2)

for result in graph.run("MATCH (p:Person) RETURN p"):
    print(result['p']['name'])
    print(result['p']['age'])

# graph.run("MATCH (p:Person) RETURN p").data()

# Working to pandas dataframe
print(DataFrame(graph.run("MATCH (p:Person) RETURN p.name,p.age").data()))
print(DataFrame(graph.run("MATCH (p:Person) RETURN p.name,p.age").to_data_frame()))
