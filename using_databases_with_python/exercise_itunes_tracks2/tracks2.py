# This application will read an iTunes export file in XML and produce a properly normalized database

import xml.etree.ElementTree as ET
import sqlite3

conn = sqlite3.connect('music.sqlite')
cur = conn.cursor()

cur.executescript('''

DROP TABLE IF EXISTS Artist;
DROP TABLE IF EXISTS Album;
DROP TABLE IF EXISTS Genre;
DROP TABLE IF EXISTS Track;

CREATE TABLE Artist (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name    TEXT UNIQUE
);

CREATE TABLE Genre (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name    TEXT UNIQUE
);

CREATE TABLE Album (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    artist_id  INTEGER,
    title   TEXT UNIQUE
);

CREATE TABLE Track (
    id  INTEGER NOT NULL PRIMARY KEY
        AUTOINCREMENT UNIQUE,
    title TEXT  UNIQUE,
    album_id  INTEGER,
    genre_id  INTEGER,
    len INTEGER, rating INTEGER, count INTEGER
);
''')

def lookup(dic, searchword):
    for i in range(len(dic)):
        if dic[i].tag == 'key' and dic[i].text == searchword:
            return dic[i+1].text
    return None # This will run only if previous return never executed

fname = input('Enter a file name: ')
if len(fname) < 1: fname = 'Library.xml'

stuff = ET.parse(fname)
all = stuff.findall('dict/dict/dict')
print ('Dict count:', len(all))

for dic in all:
    if lookup(dic, 'Track ID') is None:
        continue
    name = lookup(dic, 'Name')
    artist = lookup(dic, 'Artist')
    album = lookup(dic, 'Album')
    genre = lookup(dic, 'Genre')
    length = lookup(dic, 'Total Time')
    rating = lookup(dic, 'Rating')
    count = lookup(dic, 'Play Count')

    # Because these are primary keys not null in tables
    if name is None or artist is None or album is None or genre is None:
        continue

    print (name, artist, album, genre, length, rating, count)

    cur.execute('INSERT OR IGNORE INTO Artist (name) VALUES (?)', (artist,))
    cur.execute('SELECT id FROM Artist WHERE name = ?', (artist,))
    artist_id = cur.fetchone()[0]

    cur.execute('INSERT OR IGNORE INTO Genre (name) VALUES (?)', (genre,))
    cur.execute('SELECT id FROM Genre WHERE name = ?', (genre,))
    genre_id = cur.fetchone()[0]

    cur.execute('INSERT OR IGNORE INTO Album (artist_id, title) VALUES (?, ?)', (artist_id, album))
    cur.execute('SELECT id FROM Album WHERE title = ?', (album,))
    album_id = cur.fetchone()[0]

    cur.execute('''INSERT OR REPLACE INTO Track (title, album_id, genre_id, len, rating, count)
                   VALUES (?, ?, ?, ?, ?, ?)''', (name, album_id, genre_id, length, rating, count))

conn.commit()
