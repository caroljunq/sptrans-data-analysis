from pyspark import SparkContext
from pyspark.sql import SQLContext
from pyspark.sql.types import *
import os

path = './saidas'

paths = []

for r, d, f in os.walk(path):
    for folder in d:
        paths.append(os.path.join(r, folder))

sc = SparkContext(appName="CSV2Parquet")
sqlContext = SQLContext(sc)

traces = sqlContext.read.parquet(*paths) # pode ser um arquivo.parquet ou um diretorio
print(traces.count())

