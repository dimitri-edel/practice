import psycopg2

connection = psycopg2.connect(host="212.227.155.64",
                              dbname="chinook",
                              user="workoutapp",
                              password="w2r4k2t3!",
                              port="5432")

cursor = connection.cursor()

# cursor.execute('SELECT * FROM "Artist"')
cursor.execute('SELECT "Name" FROM "Track" WHERE "Composer" = %s', ['Queen'])

results = cursor.fetchall()

connection.close()

for result in results:
    print(result)
