import psycopg2

connection = psycopg2.connect(database="chinook")

cursor = connection.cursor()

# cursor.execute('SELECT * FROM "Artist"')
cursor.execute('SELECT "Name" FROM "Track" WHERE "Composer" = %s', ['Queen'])

results = cursor.fetchall()

connection.close()

for result in results:
    print(result)
