from haversine import haversine, Unit
import pyspark.sql.functions as F
from pyspark.sql.types import *
from pyspark.sql.window import Window

def calculate_distace(lon1,lat1,lon2,lat2,t):

    if lon2 and lat2:
        coord_1 = float(lon1),float(lat1)
        coord_2 = float(lon2),float(lat2)
        distance = haversine(coord_1,coord_2,unit=Unit.METERS)
        
        return (distance/float(t)) * 3.6
    else:
        return -1



get_distance_udf = udf(calculate_distace, FloatType())

window = Window.partitionBy("id_avl","line_id").orderBy('dt_avl')

df333 = traces_mo.select("*", get_distance_udf(F.col("trace_x"),F.col("trace_y"),F.lag(col("min_shape_coord_lon")).over(window),F.lag(col("min_shape_coord_lat")).over(window),F.col("time_variation")).alias("maie"))


