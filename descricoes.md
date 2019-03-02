# Testes com os bancos
* Fazer query e operações com: gui (algum exlorer ou aplicação), python, nodejs ou próprio shell
* Parse csv para banco (importar informaçẽos do csv)
* Métricas:
  * Tempo para armazenar 10000 e 10000 registros;
  * Memória de armanzenamento: total e por registro
* **Objetivo:** facilitar o cálculo das métricas e representação de trajetórias

# Mongo DB
## CSV:
Pode ser importado por:
* linha de comando (mongoimport);
* mongoshell
* scripts python e nodejs
* explorers (ex: 3T Studio)
Considerações:
* Não é possível definir uma estrutura de documentp para receber o csv

## Features consideráveis
* Geojson queries
* Métricas de proximidade (raio) implementadas na query

## Links úteis
* https://www.datacamp.com/community/tutorials/introduction-mongodb-python
* https://docs.mongodb.com/manual/geospatial-queries/
* https://docs.mongodb.com/manual/reference/command/dbStats/

# Neo4j
## Conceitos
* **Nodes:** entidades
* **Relações:** (edges) --> simétricas, bidirecionais
* **Propriedades:** nome: valor. Atributos das entidades, qualidade das relações e metadata.
* **Query language** --> cypher
* **Labels:** agrupa nós
* **Linked Lists:** começo/final,

## Quando utilizar
* **Relações:** quando é preciso especificar a qualidade (peso, tamanho, etc.) da relação. E/OU o valor do atributo é complexo (ex: endereço)
* **Propriedades:** quando não é necessário qualificar a relação. E o valor do atributo é simples.

## Performance
Pequenas propriedades num nó, ou uma busca numa larga string ou array pode impactar a performance.

## Cypher Language Examples
* CREATE (ee:Person { name: "Emil", from: "Sweden", klout: 99 })
* MATCH (ee:Person) WHERE ee.name = "Emil" RETURN ee;
* PROFILE MATCH (js:Person)-[:KNOWS]-()-[:KNOWS]-(surfer)
WHERE js.name = "Johan" AND surfer.hobby = "surfing"
RETURN DISTINCT surfer
* Modificadores do Return: LIMIT, DISTINCT
* MATCH (bacon:Person {name:"Kevin Bacon"})-[\*1..4]-(hollywood) RETURN DISTINCT hollywood
* MATCH p=shortestPath(
  (bacon:Person {name:"Kevin Bacon"})-[\*]-(meg:Person {name:"Meg Ryan"})
) RETURN p
* MATCH (n) DETACH DELETE n --> deleta todos os nós e relações
* MATCH (n) RETURN n --> retorna tudo

## Neo4j Commands
* :play intro --> introdução
* :sysinfo --> informações do sistema

## Features consideráveis
* Importar CSV ??
* Criar estrutra pré definida para receber CSV importado ??
* TimelineTree
* shortestPath algorith
* Neo4j Spatial/
* possível fazer query contando os hops
* fazer query dos pontos próximos

## Links importantes
* https://neo4j.com/docs/cypher-manual/current/functions/spatial/

- DÀ PRA SALVAR NO NEO e usar queries do mongo geojson?
