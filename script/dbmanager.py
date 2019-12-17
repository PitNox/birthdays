import sqlite3
import argparse
import hashlib

conn = None
cursor = None

def open_and_create():
    global conn
    global cursor
    conn = sqlite3.connect('script/example-pwd.db')
    conn = sqlite3.connect('script/pwd.db')
    cursor = conn.cursor()
    try:
        cursor.execute("SELECT * FROM user")
    except sqlite3.OperationalError:
        # Create table
        cursor.execute('''CREATE TABLE user
                     (username TEXT, password TEXT,
                      PRIMARY KEY (username))''')

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('-a', help="add a usernamename (requires -p)", required=False)
    parser.add_argument('-p', help="the username password", required=True)
    return parser.parse_args()

args = parse_args()

def save_new_username(username, password):
    global conn
    global cursor
    digest = hashlib.sha256(password.encode('utf-8')).hexdigest()
    cursor.execute("INSERT OR REPLACE INTO user VALUES (?,?)",
                   (username, digest))
    print ("Thanks for registering: you can now access the database with your credentials, use -c *username* and -p *password* to login, plus -n *name* to know name's birthday")
    conn.commit()


args = parse_args()
open_and_create()
if args.a and args.p:
    save_new_username(args.a, args.p)
conn.close()




"""
conn = None
cursor = None


def open_and_create():
    global conn
    global cursor
    conn = sqlite3.connect('example-pwd.db')
    conn = sqlite3.connect('pwd.db')
    cursor = conn.cursor()
    try:
        cursor.execute("SELECT * FROM user")
@@ -19,19 +17,4 @@ def open_and_create():
                     (username TEXT, password TEXT,
                      PRIMARY KEY (username))''')

        cursor.execute('''CREATE TABLE wallet
                     (username TEXT, balance INTEGER,
                      PRIMARY KEY (username),
                      FOREIGN KEY (username)
                        REFERENCES user(username))''')


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('-a', help="add a usernamename (requires -p)",
                        required=False)
    parser.add_argument('-p', help="the username password",
                        required=True)
    parser.add_argument('-c', help="check for a usernamename and password"
                                   "(requires -p)", required=False)
    return parser.parse_args() 
open_and_create() 
"""