import sqlite3
conn = sqlite3.connect("shifuBase.db")
cursor = conn.cursor()
print("Here's a listing of all the records in the table:")
for row in cursor.execute("SELECT rowid, * FROM list ORDER BY easy"):
    print(row)