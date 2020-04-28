import pandas as pd
import geopandas
import folium

print("maoe")

df = pd.read_csv('MO_1611.txt')
df.columns = ['server','register','line','long','lat','bus','event','nao_sei']

print("cabou")
busx = df.loc[(df['bus'] == 51661)]
# busx = df.loc[(df['bus'] == 51661) & (df['event'] == 0)]
# bus = busx[busx.apply(lambda x: x['register'].split(' ')[0] == '2016-01-01', axis=1)]
ordered_bus = busx.sort_values(['register'])
bus = ordered_bus[['register','lat','long','event']]
for hora in bus[['register','event']]:
    print(hora['register'],hora['event'])
# locations = bus[['long','lat']]
# locationlist = locations.values.tolist()
# map = folium.Map(location=[38.9, -77.05], zoom_start=12)
# for point in range(0, len(locationlist)):
#     folium.Marker(locationlist[point]).add_to(map)
# map.save('plot.html')

# import pyarrow.parquet as pq
# pandas_dataframe = pq.ParquetDataset('out_parquet2').read_pandas()
# print(pandas_dataframe.shape)