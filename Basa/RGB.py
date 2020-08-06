from flask import Flask, request, redirect, render_template, session

app = Flask(__name__)

app.secret_key= b'_5#y2L"F4Q8z\n\xec]/'

@app.route("/")
def main():
    if "color" in session:
        return render_template("colors.html", color=session['color'])
    else:
        return render_template("colors.html", color="white")

@app.route("/red")
def red():
    session["color"] = "red"
    return redirect('/')

@app.route("/green")
def green():
    session["color"] = "green"
    return redirect('/')

@app.route("/blue")
def blue():
    session["color"] = "blue"
    return redirect('/')


app.run(debug=True)