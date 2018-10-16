# This application will read roster data in JSON format, parse the file,
# and then produce an SQLite database that contains a User, Course, and Member table
# and populate the tables from the data file.

import json
import sqlite3

conn = sqlite3.connect('mentor_student.sqlite')
cur = conn.cursor()

cur.executescript('''
DROP TABLE IF EXISTS User;
DROP TABLE IF EXISTS Member;
DROP TABLE IF EXISTS Course;

CREATE TABLE User (
    id     INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name   TEXT UNIQUE
);

CREATE TABLE Course (
    id     INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    title  TEXT UNIQUE
);

CREATE TABLE Member (
    user_id     INTEGER,
    course_id   INTEGER,
    role        INTEGER,
    PRIMARY KEY (user_id, course_id)
)
''')

fname = input('Enter a file name: ')
if len(fname) < 1: fname = 'roster_data.json'

data = open(fname).read()
jdata = json.loads(data)

for item in jdata:
    name = item[0]
    coursename = item[1]
    studentormentor = item[2]

    if name is None or coursename is None: continue

    print (name, coursename, studentormentor)

    cur.execute('INSERT OR IGNORE INTO User (name) VALUES (?)', (name,))
    cur.execute('SELECT id FROM User WHERE name = ?', (name,))
    user_id = cur.fetchone()[0]

    cur.execute('INSERT OR IGNORE INTO Course (title) VALUES (?)', (coursename,))
    cur.execute('SELECT id FROM Course WHERE title = ?', (coursename,))
    course_id = cur.fetchone()[0]

    cur.execute('''INSERT OR REPLACE INTO Member (user_id, course_id, role)
                   VALUES (?, ?, ?)''', (user_id, course_id, studentormentor))

conn.commit()
