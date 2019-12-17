import sqlite3
import argparse
import hashlib
conn = None
cursor = None

def open_and_create():
    global conn
    global cursor
    conn = sqlite3.connect('pwd.db')
    cursor = conn.cursor()
    try:
        cursor.execute("SELECT * FROM user")
    except sqlite3.OperationalError:
        # Create table
        cursor.execute('''CREATE TABLE user
                     (username TEXT, password TEXT,
                      PRIMARY KEY (username))''')

open_and_create()