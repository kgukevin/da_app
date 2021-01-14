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

person = {'12-01-2020': {'Distractions': [10, 10, 1 / 3, False], 'Screen Time': [0, 24, 1 / 3, True],
                         'Diet': [10, 10, 1 / 3, False]}}


def updateReport(report):
  global person
  temp = json.loads(report)
  person = temp
  return report


def calculate_daily_score(report, date):
  '''
    report: Nested dictionary mapping date to category to [rating, max, weight]
    date: String date formatted as mm-dd-yyyy
    '''
  assert date in report.keys()
  score = 0
  for category in report[date].keys():
    data = report[date][category]
    rating = data[0]
    scale = data[1]
    weight = data[2]
    inverted = data[3]
    if inverted:
      score += (1 - rating / scale) * weight
    else:
      score += rating / scale * weight
  return str(score)


# def calculate_daily_score(ratings, weight, maxes):
#   '''
#     Ratings: list of scores per category
#     Maxes: list of maxes per category
#     Weight: list of weights per category
#
#     Returns: score for one day
#     '''
#   assert len(ratings) == len(maxes) == len(weight), 'Length incompatible'
#
#   return sum([ratings[i] / maxes[i] * weight[i] for i in range(len(ratings))])


# mixed colors later

def return_color(color, score):
  colors = {'r': 0, 'g': 1, 'b': 2}

  L = [0, 0, 0]
  L[colors[color]] = score * 255
  return tuple(L)


def get_report():
  global person
  return jsonify([person])


@app.route("/report/", methods=['GET'])
def index():
  return get_report()


@app.route("/update/", methods=['PUT'])
@cross_origin(headers=['application/json'])
def index2():
  return updateReport(request.get_data())


@app.route("/calculator/", methods=['GET'])
def index3():
  global person
  return calculate_daily_score(person, '12-01-2020')


if __name__ == '__main__':
  app.run(debug=True)
