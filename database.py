import sqlite3

def init_db():
    conn = sqlite3.connect('eliasyn.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS patients 
                 (id INTEGER PRIMARY KEY, name TEXT, medical_history TEXT)''')
    conn.commit()
    conn.close()

if __name__ == "__main__":
    init_db()
    print("Database initialized.")
