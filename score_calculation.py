#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 18 15:22:26 2020

@authors: alanyu, kevingu
"""
import json

from flask import Flask, request;
from flask_cors import CORS, cross_origin;
from flask import Flask, jsonify;

app = Flask(__name__)
CORS(app)

cat = {'Distractions': [[8, 3, 2, 1, 2, 1], 1 / 3, 10], 'Screen Time': [[2, 4, 2, 4, 1, 1], 1 / 3, 10],
       'Diet': [[10, 3, 1, 5, 1, 2], 1 / 3, 10]}


def updateCat(new_cat):
  global cat
  temp = json.loads(new_cat)
  cat = temp
  return new_cat


def calculate_score(cat, num_days):
  '''
    cat: Dictionary mapping category to [[list of scores],weight,max]
    num_days: Integer describing number of days
    '''
  assert sum([len(cat[x][0]) == num_days for x in cat]) == len(cat)

  scores = 0
  for day in range(num_days):
    scores += calculate_daily_score([cat[x][0][day] for x in cat], [cat[x][1] for x in cat], [cat[x][2] for x in cat])
  return str(scores / num_days)


def calculate_daily_score(ratings, weight, maxes):
  '''
    Ratings: list of scores per category
    Maxes: list of maxes per category
    Weight: list of weights per category

    Returns: score for one day
    '''
  assert len(ratings) == len(maxes) == len(weight), 'Length incompatible'

  return sum([ratings[i] / maxes[i] * weight[i] for i in range(len(ratings))])


# mixed colors later

def return_color(color, score):
  colors = {'r': 0, 'g': 1, 'b': 2}

  L = [0, 0, 0]
  L[colors[color]] = score * 255
  return tuple(L)


def weather_report():
  global cat
  return jsonify([cat])


@app.route("/weatherReport/", methods=['GET'])
def index():
  return weather_report()


@app.route("/inputdata/", methods=['PUT'])
@cross_origin(headers=['application/json'])
def index2():
  return updateCat(request.get_data())


@app.route("/calculator/", methods=['GET'])
def index3():
  global cat
  return calculate_score(cat, 6)


if __name__ == '__main__':
  app.run(debug=True)
