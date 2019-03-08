# Explorando bancos
* Fazer query e operações com: gui (algum exlorer ou aplicação), python, nodejs ou próprio shell
* Qual o suporte dá para fazer 'geo' queries
* Parse csv para banco (importar informaçẽos do csv)
* Features que facilitam o cálculo das métricas e modelagem de trajetórias

# Mongo DB
## CSV
Pode ser importado por:
* linha de comando (mongoimport);
* mongoshell
* scripts python e nodejs
* explorers (ex: 3T Studio)

## Funções importantes
* $geoIntersects --> seleciona geometrias que intersectam com outra geometrias
* $geoWithin --> seleciona documentos dentro da geometria dada
* $near --> seleciona pontos dentro de x metros
* $nearSphere --> mesmo que near mas usa esfera

## Múltiplos processos do mongodb
* python
* spark
* nodejs
* sharding

## Links úteis
* https://www.datacamp.com/community/tutorials/introduction-mongodb-python
* https://docs.mongodb.com/manual/geospatial-queries/
* https://docs.mongodb.com/manual/reference/operator/query-geospatial/
* https://docs.mongodb.com/manual/reference/command/dbStats/
* https://docs.mongodb.com/manual/sharding/
* https://www.linode.com/docs/databases/mongodb/build-database-clusters-with-mongodb/

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
* Importar CSV
* Criar estrutra pré definida para receber CSV importado
* ShortestPath
* Spatial queries (pontos próximos)
* Possível fazer query contando os hops

## Links importantes
* https://neo4j.com/docs/cypher-manual/current/functions/spatial/
* https://neo4j.com/developer/guide-import-csv/
* https://neo4j.com/docs/cypher-manual/current/syntax/temporal/

# Postgis
## Postgre commands
* sudo su - postgres --> conectar no postgree
* createdb mydb --> cria banco
* psql mydb --> conecta o terminal interativo no banco
* \\dt --> lista tabelas
* CREATE EXTENSION postgis --> permite usar as queries e outras ferramentas do postgis

## Postgre e Python
* http://pythonclub.com.br/postgresql-e-python3.html
* https://pythonspot.com/python-database-postgresql/
* https://www.youtube.com/watch?v=Z9txOWCWMwA
* https://www.datacamp.com/community/tutorials/tutorial-postgresql-python

## Ferramentas
* QGIS
* Consegue retornar pontos como GEOJSON ou texto
* Consegue calcular a distância dados duas coordenadas
* Cálculos de distâncias geográficas feitas na spheroid, mas é possível usar esfera
* Consigo monta uma line para a trajetória

## Funções importantes
* ST_Intersection --> retorna a geometry/geography que representa a intersecção das duas geometrias
* ST_DWithin --> retorna false ou true se a distância entre dois pontos é igual ou menor a x, ou seja,
a distância está dentro de x metros?
* ST_Distance --> calcula a distância entre dois pontos geográficos
* ST_AsGeoJSON --> retorna o ponto geográfico como uma string de geojson
* ST_Intersects --> a partir de duas geometrias, retorna true se qualquer parte de uma delas é compartilhada
* ST_Buffer --> Retorna geometry/geography que representa todos os pontos dado um ponto e um raio de distância
* select pg_size_pretty(pg_table_size('table_name')) --> memoria ocupada pela tabela

## Importando csv
* Cria tabela com headers desejados;
* COPY table_name FROM '/path_to_csv_file.csv' DELIMITERS ',' CSV;

## Múltiplos processo do postgre
* python
* nodejs

## Links importantes
* https://postgis.net/install/
* https://kitcharoenp.github.io/postgresql/postgis/2018/05/28/set_up_postgreSQL_postgis.html
* http://postgis.net/workshops/postgis-intro/geometries.html
* http://postgis.net/workshops/postgis-intro/geography.html
* https://postgis.net/docs/using_postgis_dbmanagement.html
* http://www.bostongis.com/printerfriendly.aspx?content_name=postgis_tut01
* https://www.e-education.psu.edu/spatialdb/node/1974
* http://www.postgresqltutorial.com/postgresql-data-types/
* https://tableplus.io/blog/2018/04/postgresql-import-csv-file-to-a-table.html

# Ferramentas big data 2019
Como as ferramentas de big data lidam com dados geográficos

### Links importantes
* https://cloud.google.com/bigquery/docs/gis-analyst-start
* https://cloud.google.com/bigquery/
nGalera, precisava de uma ajuda pra ver se estou pensando de um jeito bacana. Meu problema: tenho dados historicos de ônibus em .csv, vou extrair méit
# Leituras extras
* https://eng.uber.com/tech-stack-part-one/?fbclid=IwAR3_CrFTF2Oq9H_mNIbG2MYZ4Iu4Ie79bWAy0TDR0cVkHGmmFwXxhcj6b2Q


## Big Query (Google)
* Conectado cloud storage ou google drive
* Tem as mesmas features do POSTGIS, mesma queries geográficas
* Criar projeto, adiciona bigquery, cria fonte de dados, cria tabela
* Tem visualização de dados (mapa)
* Conecta com o data studio
* Integra-se com nodejs, python
* Preço Big Query: $5 per TB First terabyte (1 TB) per month is free e 0,0020 per GB Storage
* Preço One: 200GB R$9,99/mes
* Preço Cloud Storage: $0.026 GB

### Links importantes
* https://cloud.google.com/bigquery/docs/gis-intro
* https://cloud.google.com/bigquery/docs/gis-analyst-start
* https://cloud.google.com/bigquery/external-data-drive?hl=pt-br
  * https://cloud.google.com/bigquery/docs/reference/standard-sql/geography_functions
* https://cloud.google.com/bigquery/docs/gis-data

## Spark
* Geospark
* Leio de um data source e salvo em outro/mesmo formato
* Conector com Python e mongo
* Processar dados
* Possui as mesmas queries geográficas que o SQL  
* df = sqlContext.read
       .format("csv")
       .option("header", "true")
       .load("./\*.csv")

### Links importantes
* https://br.hortonworks.com/blog/magellan-geospatial-analytics-in-spark/
* https://community.hortonworks.com/questions/47988/reading-multiple-csv-files-without-headers-using-s.html

## Athena
* Conexão com o S3
* Preço: 5,00 USD por TB de dados escaneados
* Mesmas queries geográficas do SQL
* Preço S3: 0,023 USD por GB

### Links importantes
* https://aws.amazon.com/pt/athena/pricing/
* https://aws.amazon.com/pt/blogs/big-data/analyzing-data-in-s3-using-amazon-athena/
* https://docs.aws.amazon.com/pt_br/athena/latest/ug/geospatial-example-queries.html
* https://medium.com/@devopsglobaleli/introduction-17b4d0c592b6
