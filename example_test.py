import sqlite3


## Establish a connection to the database and a cursor...
connection = sqlite3.connect("data.db")
cursor = connection.cursor()


## Query data on a condition or filter...
cursor.execute("SELECT * FROM events WHERE band= 'Lions'")
print(cursor.fetchall())
print(type(rows))

## Query certain columns...
cursor.execute("SELECT band, date FROM events WHERE data= '2008.10.15'")
print(cursor.fetchall())
print(type(rows))

## Insert new rows....

new_rows = [('Cats', 'Cat City', '2008.10.17'),
            ('Hens', 'Hen City', '2008.10.17')]

cursor.executemany("INSERT INTO events VALUES(?,?,?", new_rows)
connection.commit()

## Query ALL data...
cursor.execute("SELECT * FROM events")
print(cursor.fetchall())
print(type(rows))
