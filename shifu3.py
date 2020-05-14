import sqlite3
conn = sqlite3.connect("shifuBase.db")
cursor = conn.cursor()
cursor.execute("""
                  CREATE TABLE list
                  (hard, easy,hard1, easy1,hard2, easy2,hard3, easy3,hard4, easy4)
               """)
list = [('1','2','3','4','5','6','7','8','9','10')]

cursor.executemany("INSERT INTO list VALUES (?,?,?,?,?,?,?,?,?,?)", list)
conn.commit()

print("Here's a listing of all the records in the table:")
for row in cursor.execute("SELECT rowid, * FROM list ORDER BY easy"):
    print(row)
