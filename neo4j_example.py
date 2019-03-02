# from py2neo import Graph, Node, Relationship
# from pandas import DataFrame
#
# graph = Graph(ip_addr = 'bolt://localhost:7687', username = 'neo4j', password = '123456789')
#
# p1 = Node("Person", name="eita1",age=22)
# p2 = Node("Person", name="eita2",age=24)
# p1p2 = Relationship(p1, "KNOWS", p2)
# graph.create(p1)
# graph.create(p2)
# graph.create(p1p2)
# # print(graph.__dir__())
# for node in graph.run("MATCH (p:Person) RETURN p.name, p.age"):
#     print(node['p.name'])
# graph.run("MATCH (p:Person)-[:KNOWS]->(p2:Person) RETURN p")
