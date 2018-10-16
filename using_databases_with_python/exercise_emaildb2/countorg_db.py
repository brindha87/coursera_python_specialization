# Counting Organizations
# This application will read the mailbox data (mbox.txt)
# and count the number of email messages per organization (i.e. domain name of the email address)
# using a database with the following schema to maintain the counts.
# CREATE TABLE Counts (org TEXT, count INTEGER)

import sqlite3

conn = sqlite3.connect('emaildb2.sqlite')
cur = conn.cursor()

cur.execute('DROP TABLE IF EXISTS Counts')
cur.execute('CREATE TABLE Counts (org TEXT, count INTEGER)')

# Get a file from user
fname = input('Enter a file name: ')
fhand = open(fname)
for line in fhand:
    if not line.startswith('From: '): continue
    pieces = line.split()
    org = pieces[1].split('@')[1]

    # If org not in db, insert org. Else update workinggirl
    cur.execute('SELECT org, count FROM Counts WHERE org = ?', (org,))
    row = cur.fetchone()
    if row is None:
        cur.execute('INSERT INTO Counts (org, count) VALUES (?, 1)', (org,))
    else:
        cur.execute('UPDATE Counts SET count = count + 1 WHERE org = ?', (org,))
conn.commit()

# Read db table aand print
sqlstr = 'SELECT org, count FROM Counts ORDER BY count DESC LIMIT 10'
for row in cur.execute(sqlstr):
    print (str(row[0]), row[1])

cur.close()
