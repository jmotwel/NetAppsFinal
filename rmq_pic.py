import pika


def callback(ch, method, properties, body):
    print("%r:%r" % (method.routing_key, body.decode("utf-8")))
    dataForTori = body.decode("utf-8")
    print(dataForTori)
    

# Rabbitmq setup
credentials = pika.PlainCredentials('repo-pi','netapps')
connection = pika.BlockingConnection(pika.ConnectionParameters('pumpkin-pi',
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