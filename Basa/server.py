from flask import Flask, render_template, request, redirect
import sqlite3
import time

app = Flask(__name__)

conn = sqlite3.connect("BDann.db")
c = conn.cursor()

c.execute("SELECT * FROM memes")
lenta = c.fetchall()


@app.route('/')
def start():
    conn = sqlite3.connect("BDann.db")
    c = conn.cursor()

    c.execute("SELECT * FROM memes")
    lenta = c.fetchall()

    return render_template("main.html", lenta=lenta)

@app.route("/add",  methods=["GET"])
def add_form():
    return render_template("addmeme.html")

@app.route('/add', methods=["POST"])
def add():
    #    conn = sqlite3.connect("BDann.db")
    #    c = conn.cursor()
    #    addurl = request.args.get("addurl", None)
    #    addcom = request.args.get("addcom", None)
    #    c.execute("INSERT INTO memes (url, comment, time) VALUES (?, ?, ?)", (addurl, addcom, time.time()))
    #    conn.commit()
    #    return render_template("addmeme.html")
    conn = sqlite3.connect("BDann.db")
    c = conn.cursor()
    addurl = request.form.get("addurl", None)
    addcom = request.form.get("addcom", None)
    if addurl and addcom:
        c.execute("INSERT INTO memes(url, comment,time) VALUES(?, ?,?)", (addurl, addcom, int(time.time())))
        conn.commit()
        conn.close()
        return redirect("/")
    else:
        conn.comit()
        conn.close()


@app.route('/deleted')
def deleted():
    conn = sqlite3.connect("BDann.db")
    c = conn.cursor()
    delet = request.args.get("id", None)
    c.execute("DELETE FROM memes WHERE id = ?", [delet])
    conn.commit()
    return redirect("/")


@app.route('/finder')
def find():
    conn = sqlite3.connect("BDann.db")
    c = conn.cursor()
    find = request.args.get("find", None)
    c.execute("SELECT * FROM memes WHERE comment LIKE ?", ["%" + find + "%"])
    finded = c.fetchall()
    c.execute("SELECT * FROM memes")
    lenta = c.fetchall()
    return render_template("search.html", finded=finded, lenta=lenta)


conn.commit()
conn.close()
app.run(debug=True)
