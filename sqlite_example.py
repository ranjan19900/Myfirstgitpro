import sqlite3

sqliteConnection = sqlite3.connect('first_example.db')
print("Database.connected")

cursor = sqliteConnection.cursor()
print("Database initialized")

create_table_query = """
CREATE TABLE IF NOT EXISTS emp (id integer primary key AUTOINCREMENT, name text, address text, contact integer);
"""
cursor.execute(create_table_query)

insert_table_query = """
INSERT INTO emp(name, address, contact,)
"""

cursor.execute(create_table_query)
insert_table_query = """
INSERT INTO emp(name, address, contact,) VALUE("Ranjan", "golbazar")
"""
cursor.execute(create_table_query)
insert_table_query = """
INSERT INTO emp(name, address, contact,) VALUE("Ranjan",golbazar")
"""
cursor.execute(create_table_query)
insert_table_query = """
INSERT INTO emp(name, address, contact,) VALUE("Ranjan", "golbazar",'9824737372')
"""
cursor.execute(insert_table_query)
sqliteConnection.commit()
sqliteConnection.close()