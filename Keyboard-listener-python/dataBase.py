import sqlite3

conn = sqlite3.connect('UserData.db', check_same_thread=False)

cursor = conn.cursor()

cursor.execute("CREATE TABLE IF NOT EXISTS Users (Id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, PutIn TEXT NOT NULL)")

print('Connect')