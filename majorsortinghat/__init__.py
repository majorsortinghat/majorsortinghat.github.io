import os
from flask import Flask, request, render_template, session, redirect, Blueprint

def loadRaw(rawDataFile):
    with open(rawDataFile, "r") as read_file:
        rawData = json.load(read_file)

        alldataarr = []
        alllabelsarr = []

        for person in rawData:
            if person["Major_1"] != "Undeclared":
                alllabelsarr.append(person["Major_1"])
                add_data = []
                for key in keys:
                    if key in person:
                        if person[key] != 'N/A' and person[key] != "":
                            add_data.append(int(person[key]))
                        else:
                            add_data.append(-1)
                    else:
                        add_data.append(-1)
                alldataarr.append(add_data)

                if person["Major_2"] != "":
                    alllabelsarr.append(person["Major_2"])
                    alldataarr.append(add_data)

        alldata = np.array(alldataarr)
        alllabels = np.array(alllabelsarr)
    return alldata, alllabels

def create_app(test_config = None):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        #DATABASE=os.path.join(app.instance_path, 'majorsortinghat.sqlite'),
    )
    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    from . import hats
    app.register_blueprint(hats.hats)
    app.add_url_rule('/hats', endpoint='out')

    @app.route('/')
    def index():
        return render_template('index.php')

    @app.route('/major/<major_num>')
    def major():
        return 'Major %s' % major_num

    @app.route('/hat/average', methods=['GET', 'POST'])
    def avg():
        if request.method == 'POST':
            return #TODO insert function
        else:
            return 'Hello, World!'




if name == "__main__":
    create_app()

