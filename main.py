import sqlite3

import argparse

import hashlib

import csv


conn = sqlite3.connect('script/pwd.db')

cursor = conn.cursor()


def parse_args():
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

    global conn

    global cursor

    digest = hashlib.sha256(password.encode('utf-8')).hexdigest()

    rows = cursor.execute('''SELECT * FROM user WHERE username=? and
                          password=?''', (username, digest))

    results = rows.fetchall()

    if str(username) in str(results):

        if results:

            conn.commit()

            with open(filename) as f:

                reader = csv.DictReader(f)

                for row in reader:

                    if row['name'] == args.n:

                        print ('Welcome ' + args.c + ', the birthday of '
                               + args.n
                               + ' is: ' + row['date_birth'])

        else:
            print('Name is not present, or password is invalid')

    else:
        print('Unrecognised User, please try again')


args = parse_args()

if args.c and args.p:

    check_for_username(args.c, args.p)

if args.v is True:

    print ('''This program returns the birthday of a famous person
           specified by the user. Note that the program will
           only return the birthday of people present in the
           'Data_file.csv'database. To use first run
           'script/dbmanager.py', then run main.py using python.
           Arguments are: -a: add username; -p: add password or check
           password (required); -c: check username; -v: turn on
           verbosity; n- in quotation marks, add name of
           person to research.''')

conn.close()

