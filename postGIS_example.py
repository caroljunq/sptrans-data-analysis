import psycopg2

# Connecting
conn = psycopg2.connect("dbname=mydb user=myuser")
cur = conn.cursor()

# Creating table
cur.execute("CREATE TABLE IF NOT EXISTS coordinates (name text, coordinate geometry);")
# Geography is more complex than geometry points, has more cpu costs to compute, and has less functions
# cur.execute("CREATE TABLE IF NOT EXISTS locations (name text, location geography(POINT,4326));")
# Saving data

cur.execute("INSERT INTO coordinates (name, coordinate) VALUES (%s, %s)",('Point 1', 'POINT(0 0)'))
cur.execute("INSERT INTO coordinates (name, coordinate) VALUES (%s, %s)",('Point 2', 'POINT(-15.44 23.00)'))
cur.execute("INSERT INTO coordinates (name, coordinate) VALUES (%s, %s)",('Point 3', 'POINT(18.45 27.00)'))

conn.commit()

# Retrieving data
cur.execute("SELECT name, ST_AsGeoJSON(coordinate) FROM coordinates;")
results = cur.fetchall()
for res in results:
    print(res)

# Calculating distances
cur.execute(""" SELECT ST_Distance( ST_GeographyFromText('POINT(-118.4079 33.9434)'),
    ST_GeographyFromText('POINT(2.5559 49.0083)'))
""")
result = cur.fetchall()
print(result) # result will be in meters

# Calculating if two points are x meters far from each other
cur.execute("""SELECT ST_DWithin( ST_GeographyFromText('POINT(-118.4079 33.9434)'),
    ST_GeographyFromText('POINT(2.5559 49.0083)'), 10124665.2731763)
""")
result = cur.fetchall()
print(result) # result will be a boolean

# Closing connection
cur.close()
conn.close()
