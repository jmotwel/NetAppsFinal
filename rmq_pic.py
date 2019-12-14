import pika


def callback(ch, method, properties, body):
    print("%r:%r" % (method.routing_key, body.decode("utf-8")))
    dataForTori = body.decode("utf-8")
    
    
#rmqip = sys.argv[2]

# Rabbitmq setup
credentials = pika.PlainCredentials('final-pi','netapps')
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'));
#connection = pika.BlockingConnection(pika.ConnectionParameters(SOME_IP_HERE_ON_CONSUMERS,5672,'/',credentials))
channel = connection.channel()

channel.basic_consume(queue = 'ID',
                      on_message_callback = callback,
                      auto_ack = True)

channel.start_consuming()  