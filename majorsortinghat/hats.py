from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort
import sklearn.ensemble
import sklearn.tree
import sklearn.linear_model
import numpy as np
import pickle
import math

dt = Blueprint('dtree', __name__)

with open("keys.txt", "r") as read_file:
    data = read_file.split(',')

@dt.route('/hats', methods=['GET', 'POST'])
def out():
    if request.method == 'POST':
        input_data = request.data.split('&')
        input_data = [var.split('=')[-1] for var in input_data]
        input_data = [int(var) for var in input_data]
        input_data = input_data.reshape(1, -1)

        with open("outdata.json", "r") as read_file:
            data = json.load(read_file)

        file = open('forest.sav', 'rb')
        forest = pickle.load(file)
        forest_ans = forest.predict(input_data)
        rev_forest_probs = [(1-prob) for prob in forest.predict_proba(input_data)]
        forest_dist = [prob/max(rev_forest_probs)*10 for prob in rev_forest_probs]
        file.close()

        file = open('linear.sav', 'rb')
        linear = pickle.load(file)
        linear_ans = linear.predict(input_data)
        linear_dist = [abs(dist) for dist in linear.decision_function(input_data)]
        file.close()

        return render_template('/hats/results.html', hats = hats)
    else:
        return render_template('/hats/index.html', questions = questions, qkey = qkey)

def compareValues(userInput, data):
    resultScores = {}
    avg_ans = None
    avg_score = math.inf
    for major in data:
        tempScore = 0
        for trait in userInput:
            if trait in data[str(major)]:
                tempScore += ((float(userInput[trait])-data[str(major)][trait]['Mean'])**2/(data[str(major)][trait]['SD']))
        resultScores[major] = math.sqrt(tempScore);
        if avg_score > tempScore:
            avg_ans = major
            avg_score = tempScore
    return avg_ans, resultScores
