import sqlite3

# Establish a connection to the database
conn = sqlite3.connect('data/ad_performance.db')
cursor = conn.cursor()

# Create a table to store ad performance data
cursor.execute('''
CREATE TABLE IF NOT EXISTS ad_performance (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    date TEXT NOT NULL,
    impressions INTEGER NOT NULL,
    clicks INTEGER NOT NULL,
    ctr REAL NOT NULL,
    conversions INTEGER NOT NULL
)
''')

# Insert some sample data
ad_data = [
    ('2024-08-01', 1000, 50, 0.05, 5),
    ('2024-08-02', 1200, 60, 0.05, 6),
    ('2024-08-03', 1500, 75, 0.05, 8),
]

cursor.executemany('''
INSERT INTO ad_performance (date, impressions, clicks, ctr, conversions)
VALUES (?, ?, ?, ?, ?)
''', ad_data)

# Commit the changes and close the connection
conn.commit()
conn.close()

print("Database populated successfully.")
