from flask import Flask, render_template, request, redirect, session
import sqlite3
import time

app = Flask(__name__)

conn = sqlite3.connect("BDann.db")
c = conn.cursor()

c.execute("SELECT * FROM memes")
lenta = c.fetchall()
c.execute("SELECT * FROM data")
data = c.fetchall()
print(data)

app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'


@app.route('/')
def start():
    conn = sqlite3.connect("BDann.db")
    c = conn.cursor()

    c.execute("SELECT * FROM memes")
    lenta = c.fetchall()
    c.execute("SELECT * FROM commment")
    commment = c.fetchall()
    c.execute("SELECT * FROM data")
    data = c.fetchall()
    if 'username' in session:
        return render_template("main.html", lenta=lenta, commment=commment, data=data, user=session["username"])
    else:
        return redirect("/login")


@app.route("/add", methods=["GET"])
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
    c.execute("SELECT * FROM data WHERE login = ?", [session["username"]])
    user = c.fetchall()
    print(user[0][0])
    if addurl and addcom:
        c.execute("INSERT INTO memes(url, comment, time, author_id) VALUES(?, ?,  ?, ?)",
                  (addurl, addcom, int(time.time()), user[0][0]))
        conn.commit()
        conn.close()
        return redirect("/")
    else:
        return redirect("/add")
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


@app.route("/add_coment", methods=["POST"])
def add_coment():
    conn = sqlite3.connect("BDann.db")
    c = conn.cursor()
    id_com = request.args.get("id", None)
    com1 = request.form.get("com1", None)
    c.execute("SELECT id FROM data WHERE login = ?", [session["username"]])
    ai = c.fetchall()
    c.execute("INSERT INTO commment (text, meme_if) VALUES (?, ?)", (com1, id_com))
    conn.commit()
    conn.close()
    # return render_template("main.html", comm=comm)
    return redirect("/")


@app.route("/del")
def delet():
    conn = sqlite3.connect("BDann.db")
    c = conn.cursor()
    d = request.args.get("id1", None)
    c.execute("DELETE FROM commment WHERE id = ?", [d])
    conn.commit()
    conn.close()
    return redirect("/")


@app.route('/login', methods=['GET', 'POST'])
def login():
    conn = sqlite3.connect("BDann.db")
    c = conn.cursor()
    if request.method == 'POST':
        for i in data:
            if request.form['login'] == i[1] and request.form['pass'] == i[2]:
                session['username'] = request.form['login']
                session['password'] = request.form['pass']
                return redirect('/')
        for i in data:
            if request.form['login'] != i[1] and request.form['pass'] != i[2]:
                return redirect('/login')
    else:
        return render_template("login.html")


@app.route('/logout')
def logout():
    # remove the username from the session if it's there
    session.pop('username', None)
    return redirect("/")


@app.route("/reg", methods=["POST"])
def reg():
    if request.form["rlogin"] and request.form["rpass"]:
        conn = sqlite3.connect("BDann.db")
        c = conn.cursor()
        rlog = request.form["rlogin"]
        rpass = request.form["rpass"]
        c.execute("INSERT INTO data(login, password) VALUES(?, ?)", (rlog, rpass,))
        conn.commit()
        conn.close()
        return redirect("/")
    else:
        return redirect("reg")


@app.route("/reg", methods=["GET"])
def preg():
    return render_template("registration.html")


conn.commit()
conn.close()
app.run(debug=True)
