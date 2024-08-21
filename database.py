import sqlite3

def get_connection():
    conn = sqlite3.connect('data/ad_performance.db')
    return conn


def create_tables(conn):
    """Create tables if they don't exist."""
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS ad_performance (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            date TEXT,
            impressions INTEGER,
            clicks INTEGER,
            conversions INTEGER
        )
    ''')
    conn.commit()

def insert_data(conn, date, impressions, clicks, conversions):
    """Insert data into the ad_performance table."""
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO ad_performance (date, impressions, clicks, conversions)
        VALUES (?, ?, ?, ?)
    ''', (date, impressions, clicks, conversions))
    conn.commit()

def get_ad_performance(conn, start_date, end_date):
    """Retrieve ad performance data between specified dates."""
    cursor = conn.cursor()
    cursor.execute('''
        SELECT date, impressions, clicks, conversions
        FROM ad_performance
        WHERE date BETWEEN ? AND ?
        ORDER BY date
    ''', (start_date, end_date))
    rows = cursor.fetchall()
    return rows
