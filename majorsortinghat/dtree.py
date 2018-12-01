from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort
import sklearn.ensemble
import numpy as np

dt = Blueprint('dtree', __name__)

with open("keys.txt", "r") as read_file:
    data = json.load(read_file).split(',')

@dt.route('/hat/dtree', methods=['GET', 'POST'])
def dtreeout():
    if request.method == 'POST':
    	dtree = sklearn.ensemble.RandomForestClassifier(n_estimators=100, random_state=23)
		dtree = dtree.fit(values, labels)
		ans = dtree.predict(dt6_2Input.reshape(1,-1)))
        return #TODO insert function
    else:
        return 'Hello, World!'

