import pika

# Rabbitmq setup
credentials = pika.PlainCredentials('repo-pi','netapps')
connection = pika.BlockingConnection(pika.ConnectionParameters('pumpkin-pi',
                                                               5672,
                                                               '/',
                                                               credentials));

channel = connection.channel()

# Put these into if statements
# will send a message to the relevant queue (ID for pics, Score for high scores)

channel.basic_publish(exchange='Pokemon',
                      routing_key='ID',
                      body='10')

channel.basic_publish(exchange='Pokemon',
                      routing_key='Score',
                      body='8327')
