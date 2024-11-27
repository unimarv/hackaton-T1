import sqlite3

db_file = 'gold.db'
conn = sqlite3.connect(db_file)
cursor = conn.cursor()
cursor.execute("SELECT * FROM gold")
rows = cursor.fetchall()
for row in rows:
    print(row)
cursor.close()
conn.close()