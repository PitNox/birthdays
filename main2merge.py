import sqlite3
import argparse
import hashlib
conn = None
cursor = None

"""---------------------------------------------------------------------------------------------------------------------------------------------------------------"""

def open_and_create():
    global conn
    global cursor
    conn = sqlite3.connect('example-pwd.db')
    cursor = conn.cursor()
    try:
        cursor.execute("SELECT * FROM user")
    except sqlite3.OperationalError:
        # Create table
        cursor.execute('''CREATE TABLE user
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


def save_new_username_correct(username, password):
    global conn
    global cursor
    digest = hashlib.sha256(password.encode('utf-8')).hexdigest()
    cursor.execute("INSERT OR REPLACE INTO user VALUES (?,?)",
                   (username, digest))
    cursor.execute("INSERT OR REPLACE INTO wallet VALUES (?,?)",
                   (username, 10))
    conn.commit()


def check_for_username_correct(username, password):
    global conn
    global cursor
    digest = hashlib.sha256(password.encode('utf-8')).hexdigest()
    rows = cursor.execute("SELECT * FROM user WHERE username=? and password=?",
                          (username, digest))
    results = rows.fetchall()
    
    if str(username) in str(results):

        if results:
            conn.commit()
            b = cursor.execute ("SELECT balance FROM user JOIN wallet WHERE user.username = wallet.username")
            print( "User is present, password is valid, balance is %s" % b.fetchall()[0][0])
        else:
            print ("User is not present, or password is invalid")

    else:
        print ("Unrecognised User, please try again")

#add name argument to be asked

args = parse_args()
open_and_create()
if args.a and args.p:
    #save_new_username_vulnerable(args.a, args.p)
    save_new_username_correct(args.a, args.p)
elif args.c and args.p:
    #check_for_username_vulnerable(args.c, args.p)
    check_for_username_correct(args.c, args.p)
conn.close() 

"""-------------------------------------------------------------------------------------------------------------------------------------------------------------"""