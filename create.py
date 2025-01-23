import sqlite3

# Connect to or create the database file
connection = sqlite3.connect('auth.db')
cursor = connection.cursor()

# Create the users table
cursor.execute('''
    CREATE TABLE users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT NOT NULL UNIQUE,
        password TEXT NOT NULL
    )
''')

# Insert sample data
sample_data = [
    ('admin', 'admin123'),
    ('testuser', 'testpass'),
    ('johndoe', 'password123')
]

cursor.executemany('INSERT INTO users (username, password) VALUES (?, ?)', sample_data)
connection.commit()

# Close the connection
connection.close()

print("auth.db created successfully with sample data!")
