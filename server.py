from flask import Flask, jsonify
from flask import request, render_template
from flask import make_response
from flask_json import FlaskJSON, JsonError, json_response, as_json


app = Flask(__name__)
FlaskJSON(app)

@app.route('/')
def index():
	return render_template('index.html')


@app.route('/team',methods=['POST'])
def get_team():
    data = request.get_json(force=True)
    try:
	print(data)
    except (KeyError,TypeError,ValueError):
	raise JsonError(description='Invalid value')
    return json_response(value = 1)

@app.route('/pokemon',methods=['POST'])
def get_pokemon():
    data = request.get_json(force=True)
    try:
	print(data)
    except (KeyError,TypeError,ValueError):
	raise JsonError(description='Invalid value')
    return json_response(value = 1)

if __name__=='__main__':

    app.run(debug=True, port=8000, host='0.0.0.0')
