from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def rezume():
    return render_template('Page.html')

@app.route('/GoTo')
def GoTo():
    return 'Welcome to GoTo'

@app.route('/resume')
def resume():
    return render_template('resume.html')

@app.route('/serials')
def FavoritSerials():
    return render_template('serials.html')

if __name__ == '__main__':
    app.run(debug=True)