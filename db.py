import sqlite3

DB_NAME = "expenses.db"

def init_db():
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS expenses (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    date TEXT,
                    category TEXT,
                    amount REAL,
                    description TEXT
                )''')
    conn.commit()
    conn.close()

def add_expense(date, category, amount, description):
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute("INSERT INTO expenses (date, category, amount, description) VALUES (?, ?, ?, ?)",
              (date, category, amount, description))
    conn.commit()
    conn.close()

def get_expenses():
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute("SELECT * FROM expenses ORDER BY date DESC")
    rows = c.fetchall()
    conn.close()
    return rows

