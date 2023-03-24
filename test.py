import sqlite3

db = sqlite3.connect("eten.sqlite")
cursor = db.cursor()

cursor.execute("DELETE FROM login WHERE mail='hello';")
db.commit()

var = cursor.execute("SELECT * FROM login;")

for row in var:
    print(row)

db.close()