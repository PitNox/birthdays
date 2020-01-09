"""This is the main code for the project Birthdays. The code is based on an
SQLite databse to check for user authentication and a python function with
the arparse module to return the desired information"""

import sqlite3

import argparse

import hashlib

import csv


conn = sqlite3.connect('script/pwd.db')
cursor = conn.cursor()


def parse_args():
    """collecting user input into arguments with argparse module"""
    parser = argparse.ArgumentParser()
    parser.add_argument('-p', help='the username password',
                        required=True)

    parser.add_argument('-c', help='check for a usernamename and password'
                        '(requires -p)',
                        required=False)

    parser.add_argument('-n', help='''Insert name in quotation marks to get
                        birthday''',
                        required=False)

    parser.add_argument('-v', help='increase verbosity', default=False,
                        action='store_true',
                        required=False)

    return parser.parse_args()


args = parse_args()

filename = 'Data_file.csv'


def check_for_username(username, password):
    """authenticating the user and returning correct birthday"""

    global conn

    global cursor

    if args.v is True:
        print ("authenticating user...")

    digest = hashlib.sha256(password.encode('utf-8')).hexdigest()

    rows = cursor.execute('''SELECT * FROM user WHERE username=? and
                          password=?''', (username, digest))

    results = rows.fetchall()

    if str(username) in str(results):

        if args.v is True:
            print ("user authenticated. Welcome " + args.c + ". ")

        if results:

            conn.commit()

            if args.v is True:
                print ("fetching birthday data...")

            with open(filename) as f:

                reader = csv.DictReader(f)

                for row in reader:

                    if row['name'] == args.n:

                        print ('The birthday of ' + args.n +
                               ' is: ' + row['date_birth'])

        else:
            print('Name is not present, or password is invalid')

    else:
        print('Unrecognised User, please try again')


args = parse_args()

if args.n:
    if args.c and args.p:
        print ("")
        check_for_username(args.c, args.p)
        print ("")
else:
    print ("")
    print ("Please insert -n argument 'name' as follows: -n '*name*' ")
    print ("")
    conn.close()
