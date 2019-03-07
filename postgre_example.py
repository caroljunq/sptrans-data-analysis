import psycopg2

# Connecting
conn = psycopg2.connect("dbname=mydb user=myuser")
cur = conn.cursor()

# Creating table
cur.execute("CREATE TABLE IF NOT EXISTS person (id serial PRIMARY KEY, name text, age integer);")

# Inserting data
cur.execute("INSERT INTO person (name, age) VALUES (%s, %s)",("O'Relly", 60))
cur.execute("INSERT INTO person (name, age) VALUES (%s, %s)",('Regis', 35))
conn.commit()

# Retrieving data
cur.execute("SELECT * FROM person;")
results = cur.fetchall()
for res in results:
    print(res)

# Closing connection
cur.close()
conn.close()
