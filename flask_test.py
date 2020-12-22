from flask import Flask;
from flask_cors import CORS;
from flask import Flask, jsonify;

app = Flask(__name__)
CORS(app)

weather = {
  "data": [
    {
      "day": "1/6/2019",
      "temperature": "23",
      "windspeed": "16",
      "event": "Sunny"
    },
    {
      "day": "1/7/2019",
      "temperature": "20",
      "windspeed": "9",
      "event": "Thunderstorm"
    },
    {
      "day": "1/8/2019",
      "temperature": "40",
      "windspeed": "96",
      "event": "Rainy"
    },
    {
      "day": "1/9/2019",
      "temperature": "73",
      "windspeed": "0",
      "event": "Sunny"
    }
  ]
}


def weather_report():
    global weather
    return jsonify([weather])


@app.route("/weatherReport/", methods=['GET'])
def index():
    return weather_report()


if __name__ == '__main__':
    app.run(debug=True)
