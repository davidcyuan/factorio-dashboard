import sqlite3
from datetime import datetime
import os

DATABASE_NAME = "factory.db"


def get_connection():
    """Get a connection to the SQLite database."""
    return sqlite3.connect(DATABASE_NAME)


def init_db():
    """Initialize the database and create tables if they don't exist."""
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS production_log (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
            product_name TEXT NOT NULL,
            quantity INTEGER NOT NULL,
            assembler_id TEXT,
            utilization_rate REAL,
            defect_count INTEGER DEFAULT 0,
            lead_time REAL
        )
    """)

    conn.commit()
    conn.close()


def log_production(product_name, timestamp, quantity, assembler_id=None, utilization_rate=None, defect_count=0, lead_time=None):
    """Log a production entry."""
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO production_log (product_name, timestamp, quantity, assembler_id, utilization_rate, defect_count, lead_time)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    """, (product_name, timestamp, quantity, assembler_id, utilization_rate, defect_count, lead_time))

    conn.commit()
    conn.close()


def get_all_logs():
    """Retrieve all production logs."""
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM production_log ORDER BY timestamp DESC")
    rows = cursor.fetchall()
    conn.close()
    return rows

def get_logs_by_product(product_name):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM production_log WHERE product_name = ? ORDER BY timestamp DESC", (product_name,))
    rows = cursor.fetchall()
    conn.close()
    return rows

def clear_logs():
    """Clear all production logs (for testing/reset)."""
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM production_log")
    conn.commit()
    conn.close()


if __name__ == "__main__":
    # Initialize database on direct execution
    init_db()
    print(f"✓ Database '{DATABASE_NAME}' initialized")
