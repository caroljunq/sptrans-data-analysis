# Tutorial
# http://blogs.quovantis.com/how-to-convert-csv-to-parquet-files/

from pyspark import SparkContext
from pyspark.sql import SQLContext
from pyspark.sql.types import *
import glob, os

sc = SparkContext(appName="CSV2Parquet")
sqlContext = SQLContext(sc)

def generate_parquet(file_name):
    print("Gerando o parquet para o arquivo " + file_name)
    parquet_name = file_name + "_outparquet"

    schema = StructType([
        StructField("server_date", StringType(), True),
        StructField("avl_date", StringType(), True),
        StructField("line_id", StringType(), True),
        StructField("longitude", StringType(), True),
        StructField("latitude", StringType(), True),
        StructField("avl_id", StringType(), True),
        StructField("event", StringType(), True),
        StructField("point", StringType(), True)
    ])

    rdd = sc.textFile('../'+file_name+".txt").map(lambda line: line.split(",")[1:])
    df = sqlContext.createDataFrame(rdd, schema)
    df.write.parquet(parquet_name)

# obtendo lista de .txt do diretorio,
print("Lendo arquivos do diretorio")
file_list = []
os.chdir("../")
for file_name in glob.glob("*.txt"):
    file_list.append(file_name.split('.')[0])

# gerando os parquet dos csv
for file_name in file_list:
    generate_parquet(file_name)


# Outro jeito
# df_pandas = pd.read_csv('example.csv')
# df_pandas.to_parquet('usando_pandas.parquet')

# print(busao.select(busao['event'] == 0).count())
# Queries SQL, falata descobrir como faz as queries no script python
# busao.registerTempTable('busao')
# results =  spark.sql("SELECT * FROM busao WHERE line _id = 2179")
# print(results.head(10))
