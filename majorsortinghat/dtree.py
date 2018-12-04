from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort
import sklearn.ensemble
import numpy as np
import pickle

dt = Blueprint('dtree', __name__)

with open("keys.txt", "r") as read_file:
    data = json.load(read_file).split(',')

@dt.route('/hat/dtree', methods=['GET', 'POST'])
def dtreeout():
    if request.method == 'POST':
        input_data = request.data.split('&')
        input_data = [var.split('=')[-1] for var in input_data]
        input_data = [int(var) for var in input_data]
        file = open('dtree.sav', 'rb')
        dtree = pickle.load(file)
        ans = dtree.predict(input_data)
        return #TODO insert function
    else:
        return 'Hello, World!'

