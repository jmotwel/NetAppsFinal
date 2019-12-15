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

channel.basic_consume(queue = 'ID',
                      on_message_callback = callback,
                      auto_ack = True)

channel.start_consuming()  
