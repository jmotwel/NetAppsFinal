from flask import Flask, jsonify
from flask import request, render_template
from flask import make_response
from flask_json import FlaskJSON, JsonError, json_response, as_json
import pika
import json
from pymongo import MongoClient


credentials = pika.PlainCredentials('repo-pi','netapps')


connection1 = pika.BlockingConnection(pika.ConnectionParameters('jamies-raspberrypi',
                                                               5672,
                                                               '/',
                                                               credentials));
connection2 = pika.BlockingConnection(pika.ConnectionParameters('jamies-raspberrypi',
						       5672,
						       '/',
						       credentials));						       
channel1 = connection1.channel()
channel2 = connection2.channel()

channel1.exchange_declare(exchange='Pokemon',
                         exchange_type='direct',
                         durable=False)
channel2.exchange_declare(exchange='Pokemon',
                         exchange_type='direct',
                         durable=False)


client = MongoClient('localhost', 27017)
db=client.test

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
	
	channel1.basic_publish(exchange='Pokemon',
		      routing_key='Score',
                      body=json.dumps(data))
	db.team.insert_one(data)
    except (KeyError,TypeError,ValueError):
	raise JsonError(description='Invalid value')
    return json_response(value = 1)


@app.route('/pokemon',methods=['POST'])
def get_pokemon():
    data = request.get_json(force=True)

    print(data)
    
    #print(result)
    channel2.basic_publish(exchange='Pokemon',
		  routing_key='ID',
		  body=json.dumps(data))
    db.pokemon.insert_one(data)
    return json_response(value = 1)

if __name__=='__main__':

    app.run(debug=True, port=8000, host='0.0.0.0')
