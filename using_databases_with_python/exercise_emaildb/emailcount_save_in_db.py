# This application will read the mailbox data and count the number of email messages per sender 

import sqlite3

# Form a connection and cursor
conn = sqlite3.connect('emaildb.sqlite')
cur = conn.cursor()

# Prepare the table
cur.execute('DROP TABLE IF EXISTS Counts')
cur.execute('CREATE TABLE Counts (email TEXT, count INTEGER)')

# Get file name from user
fname = input('Enter file name: ')
if len(fname) < 1: fname = 'mbox-short.txt'

# Read the file and extract email
fhand = open(fname)
for line in fhand:
    if not line.startswith('From: '): continue
    pieces = line.split()
    email = pieces[1]

    # If this email NOT already present in the database, make an entry. Otherwise update existing copy
    cur.execute('''SELECT count
                   from Counts
                   WHERE email = ?''', (email,))
    row = cur.fetchone()
    if row is None:
        conn.execute('''INSERT INTO Counts (email, count)
                        VALUES (?, 1)''', (email,))
    else:
        conn.execute('''UPDATE Counts
                        SET count = count + 1
                        WHERE email = ?''', (email,))
    # conn.commit()
conn.commit()

# Read the table and print
sqlstr = '''SELECT email, count
            FROM Counts
            ORDER BY count
            DESC LIMIT 10'''
for row in cur.execute(sqlstr):
    print (str(row[0]), row[1])

cur.close()
