from flask import Flask, request, render_template, session, redirect

app = Flask(__name__)

app.secret_key = b'DEVELOPMENT_KEY' #TODO: CHANGE FOR PRODUCTION

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/major/<major_num>')
def major():
    return 'Major %s' % major_num

@app.route('/hat/average', methods=['GET', 'POST'])
def avg():
    if request.method == 'POST':
        return #TODO insert function
    else:
        return 'Hello, World!'

@app.route('/hat/dtree', methods=['GET', 'POST'])
def dtree():
    if request.method == 'POST':
        return #TODO insert function
    else:
        return 'Hello, World!'

@app.route('/hat/ml', methods=['GET', 'POST'])
def ml():
    if request.method == 'POST':
        return #TODO insert function
    else:
        return 'Hello, World!'

if name == '__main__':
    app.run()