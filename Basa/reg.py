from flask import Flask, session, redirect, url_for, request, render_template
import sqlite3
from markupsafe import escape

app = Flask(__name__)

app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

conn = sqlite3.connect("BDann.db")
c = conn.cursor()
c.execute("SELECT * FROM data")
data = c.fetchall()


@app.route('/')
def index():
    if 'username' in session:
        return render_template("glav.html")
    return render_template("login.html")


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        session['username'] = request.form['login']
        session['password'] = request.form['pass']
        return redirect(url_for('index'))
    return '''
        <form method="post">
            <p><input type=text name=username>
            <p><input type=submit value=Login>
        </form>
    '''


@app.route('/logout')
def logout():
    # remove the username from the session if it's there
    session.pop('username', None)
    return redirect(url_for('index'))


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


@app.route("/reg", methods=["GET"])
def preg():
    return render_template("registration.html")


app.run(debug=True)
