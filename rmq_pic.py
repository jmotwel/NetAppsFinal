import pika

# Rabbitmq setup
credentials = pika.PlainCredentials('repo-pi','netapps')
connection = pika.BlockingConnection(pika.ConnectionParameters('jamies-raspberrypi',
                                                               5672,
                                                               '/',
                                                               credentials));
channel = connection.channel()

channel.exchange_declare(exchange='Pokemon',
                         exchange_type='direct',
                         durable=False)


while (1):
    
    curVal = channel.basic_get(queue='ID', auto_ack=True)
    if curVal != (None, None, None):
        dataForTori = curVal[2]
        print(dataForTori.decode("utf-8"))
