from flask import render_template, request, Flask
import random

app = Flask(__name__)

goroda = {}

@app.route('/weather')
def generate():

    town = request.args.get('town', None)
    m = ["Солнечно", "Пасмурно", "Ветренно", "Переменная облачность"]
    im = ["/static/sunny.jpeg", "/static/rainy.png", "/static/windy.png", "/static/PP.jpeg"]

    if town not in goroda:
        temparature = random.randint(-40, +48)
        state = random.randint(0, 3)

        goroda[town] = {
            "temperature": temparature,
            "image": im[state],
            "humidity": m[state]
        }
        return render_template("weather.html", word=town, temp=temparature, sos=m[state], weather_image=im[state])

    else:
        return render_template("weather.html", word=town, temp=goroda[town]["temperature"], sos=goroda[town]["humidity"], weather_image=goroda[town]["image"])


@app.route('/')
def start():
        return render_template('ww.html')


app.run(debug=True)
