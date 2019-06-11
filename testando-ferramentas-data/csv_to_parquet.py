from pyspark import SparkContext
from pyspark.sql import SQLContext
from pyspark.sql.types import *
import pandas as pd
import pyspark
import time
import datetime

if __name__ == "__main__":
    sc = SparkContext(appName="CSV2Parquet")
    sqlContext = SQLContext(sc)

    # schema = StructType([
    #         # StructField("row_id", StringType(), True),
    #         StructField("server_date", StringType(), True),
    #         StructField("avl_date", StringType(), True),
    #         StructField("line_id", StringType(), True),
    #         StructField("lng", StringType(), True),
    #         StructField("lat", StringType(), True),
    #         StructField("bus_id", StringType(), True),
    #         StructField("event", StringType(), True),
    #         StructField("something", StringType(), True)
    # ])


    # rdd = sc.textFile("MO_1611.txt").map(lambda line: line.split(","))
    # df = sqlContext.createDataFrame(rdd, schema)
    # df.write.parquet('out_parquet2')

# Outro jeito
# df_pandas = pd.read_csv('example.csv')
# df_pandas.to_parquet('usando_pandas.parquet')

# Lendo o diretorio criado
busao = sqlContext.read.parquet("out_parquet2") # pode ser um arquivo.parquet ou um diretorio
# print(busao.select("event").distinct().count())
print(busao.select(busao['event'] == 0).count())


# Queries SQL, falata descobrir como faz as queries no script python
# busao.registerTempTable('busao')
# results =  spark.sql("SELECT * FROM busao WHERE line _id = 2179")
# print(results.head(10))
