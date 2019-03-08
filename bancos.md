<!-- $theme: gaia -->

# Modelagem de trajetórias
## Tecnologias

---
# MongoDB
* NoSQL
* Python e Nodejs
* **Query geográficas:** $geoIntersects, $geoWithin, $near, $nearSphere
* Importar csv: linha de comando, scrips ou softwares (explorers)
* Resultados:
	* Cada registro: 180 B
	* 10000 registros: 1,7MB

----
# Neo4j
* Baseado em grafo: nós, relações, propriedades
* Cypher Query Language
* Features: shortestPath, spatial queries e hops
![55%](https://s3.amazonaws.com/dev.assets.neo4j.com/wp-content/uploads/cypher_graph_v1.jpg)
----
# PostGIS
* Queries geo com SQL
* Funções: intersection, dwithin, distance, buffer
* Conecta com python e nodejs
* Possui cálculo esfera ou esferóide
-----
# Ferramentas BigData
----------
# Big Query (Google)
* Data sources: cloud storage ou gdrive ou fontes externas
* Mesmas queries geográficas que SQL
* Nodejs ou python
* Importo o csv
* Preços 
	* storage (0,0020/GB)
	* consultas US$5,00/TB
	* torage Cloud ou Gdrive
-----
# Spark 
* Geospark
* Distríbuido --> cria partições
* Python, mongo e nodejs
* Possui queries SQL
![](https://dev.acquia.com/sites/default/files/blog/apache_spark_logo_big_0.png)
------
# Athena AWS
* Conecta com S3 AWS (csvs)
* Possui queries geográficas SQL
* Preços:
	* S3: 0,023 USD/GB
	* Consultas: 5,00 USD/TB
![55%](https://i1.wp.com/www.techtrainees.com/wp-content/uploads/2018/10/12.png?resize=800%2C445&ssl=1)
---
# Amazon EMR
* Plataforma de cluster que gerencia a execução de estruturas de Big Data ex: Spark, python, nodejs,
* Conecta com S3
* Gerenciamento do cluster YARn default
![80%](https://dmhnzl5mp9mj6.cloudfront.net/bigdata_awsblog/images/Bioinformatics_Image_1.PNG)