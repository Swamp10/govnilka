import sqlite3
import time
from flask import Flask, request, render_template

app = Flask(__name__)
2
conn = sqlite3.connect('BDann.db')
c = conn.cursor()
print("Write:")
print("1. to bring out all the memes")
print("2. add meme")
print("3. Search by comments")
print("4. Delete meme")

a = int(input())

c.execute("SELECT * FROM memes")
result = c.fetchall()

if a == 1:
    for line in result:
        print("id", line[0])
        print("url", line[1])
        print("comment", line[2])
        print("time", line[3])

if a == 2:
    print("Send URL and comment")
    url = str(input())
    comm = str(input())
    c.execute("INSERT INTO memes (url, comment, time) VALUES (?, ?, ?)", (url, comm, time.time()))

if a == 3:
    print("Enter a comment for the desired meme")
    comsearch = str(input())
    c.execute("SELECT * FROM memes WHERE comment = ?", [comsearch])
    print(*(c.fetchall()))

if a == 4:
    print()
    deletmem = int(input())
    c.execute("DELETE FROM memes WHERE id = ?", [deletmem])






conn.commit()
conn.close()