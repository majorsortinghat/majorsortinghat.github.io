from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for, session
)
from werkzeug.exceptions import abort
import sklearn.ensemble
import sklearn.tree
import sklearn.linear_model
import numpy as np
import pickle
import math
import json
import os
from . import APP_STATIC
from wtforms import Form, RadioField, StringField, validators

hats = Blueprint('hats', __name__)


with open(os.path.join(APP_STATIC, 'keys.txt'), 'r') as file:
    keys = file.read().split(',')

with open(os.path.join(APP_STATIC, 'questions.txt'), 'r') as file:
    questions = file.read().split(',')

with open(os.path.join(APP_STATIC, 'outdata.json'), 'r') as file:
    avg_model = json.load(file)

with open(os.path.join(APP_STATIC, 'forest.sav'), 'rb') as file:
    forest = pickle.load(file)

with open(os.path.join(APP_STATIC, 'linear.sav'), 'rb') as file:
    linear = pickle.load(file)

@hats.route('/hats', methods=['GET', 'POST'])
def out():
    form = sortingQuiz(name = u"bad")
    if request.method == "POST":

        session['input_data'] = np.array([field.data for field in form.fields])
        return redirect(url_for('results'), debug = session[input_data])
        model_input_data = session['input_data'].reshape(1, -1)

        #with open("keys.txt", "r") as file:
        #    keys = file.split(',')

        #with open("outdata.json", "r") as file:
        #    avg_model = json.load(file)
        session['avg_ans'], session['avg_dist'] = compareValues(session['input_data'], avg_model)

        #with open('forest.sav', 'rb') as file:
        #    forest = pickle.load(file)
        #forest_ans = forest.predict(model_input_data)
        session['forest_ans'] = forest.predict(model_input_data)
        rev_forest_probs = [(1-prob) for prob in forest.predict_proba(model_input_data)]
        session['forest_dist'] = [prob/max(rev_forest_probs)*10 for prob in rev_forest_probs]

        #with open('linear.sav', 'rb') as file:
        #    linear = pickle.load(file)
        session['linear_ans'] = linear.predict(model_input_data)
        session['linear_dist'] = [abs(dist) for dist in linear.decision_function(model_input_data)]

        return redirect(url_for('results'))
    else:
        return render_template('/hats/index.html', form = form)

@hats.route('/hats/results')
def results():
    return render_template('/hats/results.html')

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

class sortingQuiz(Form):
    for i in range(len(questions)):
        exec(keys[i] + " = RadioField(questions[i], choices = [(val, '') for val in range(-2,3)])")
