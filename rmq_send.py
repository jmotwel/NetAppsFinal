import pika
import socket
import sys


def callback(ch, method, properties, body):
    print("%r:%r" % (method.routing_key, body.decode("utf-8")))
    

# Rabbitmq setup
credentials = pika.PlainCredentials('final-pi','netapps')
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'));
channel = connection.channel()

#channel.exchange_declare(exchange='Pokemon',
#                         exchange_type='direct',
#                         durable=True)

# Put these into if statements
# will send a message to the relevant queue (ID for pics, Score for high scores)

channel.basic_publish(exchange='Pokemon',
                      routing_key='ID',
                      body='10')

channel.basic_publish(exchange='Pokemon',
                      routing_key='Score',
                      body='8327')
