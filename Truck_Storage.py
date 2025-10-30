
import sqlite3 as sql
import toga
from toga.style import Pack

# Connect to (or create) a database file
conn = sql.connect("products.db")

# Create a cursor object to interact with the database
cursor = conn.cursor()
#
# # Create the table
# cursor.execute("""
# CREATE TABLE products (
#     id INTEGER PRIMARY KEY AUTOINCREMENT,
#     product_name TEXT NOT NULL,
#     length INTEGER NOT NULL,
#     width INTEGER NOT NULL,
#     weight INTEGER NOT NULL)
# """)
#
# # Insert some test data
# sample_data = [
#     ("AAA", 120, 80, 451),
#     ("BBB", 120, 80, 547),
#     ("CCC", 120, 100, 657)
# ]
#
# cursor.executemany("""
# INSERT INTO products (product_name, length, width, weight)
# VALUES (?, ?, ?, ?)
# """, sample_data)

# Delete specific row by ID

# cursor.execute("DELETE FROM products WHERE id = 6")
conn.commit()



cursor.execute("SELECT * FROM products")
rows = cursor.fetchall()

for row in rows:
    print(row)
