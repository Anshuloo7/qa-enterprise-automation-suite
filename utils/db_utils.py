import sqlite3
import os

DB_PATH = os.path.join(os.path.dirname(__file__), "..", "db", "products.db")
os.makedirs(os.path.dirname(DB_PATH), exist_ok=True)

class DBUtils:
    def __init__(self):
        self.conn = sqlite3.connect(DB_PATH)
        self.cursor = self.conn.cursor()
        self.create_tables()

    def create_tables(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS products (
                id INTEGER PRIMARY KEY,
                title TEXT,
                price REAL,
                category TEXT
            )
        """)
        self.conn.commit()

    def insert_product(self, product):
        self.cursor.execute("""
            INSERT OR REPLACE INTO products (id, title, price, category)
            VALUES (?, ?, ?, ?)
        """, (product['id'], product['title'], product['price'], product['category']))
        self.conn.commit()

    def fetch_all_products(self):
        self.cursor.execute("SELECT * FROM products")
        return self.cursor.fetchall()

    def fetch_product_by_id(self, product_id):
        self.cursor.execute("SELECT * FROM products WHERE id = ?", (product_id,))
        return self.cursor.fetchone()

    def clear_table(self):
        self.cursor.execute("DELETE FROM products")
        self.conn.commit()

    def close(self):
        self.conn.close()