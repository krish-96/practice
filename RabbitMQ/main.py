import pika
from datetime import datetime

connection_parameters = pika.ConnectionParameters('localhost')
connection = pika.BlockingConnection(connection_parameters)
channel = connection.channel()

channel.queue_declare(queue='simple')
message = "Now the time is %s" % datetime.now().strftime('%Y-%m-%d %H:%M:%s')

channel.basic_publish(exchange='', routing_key='simple', body=message)

connection.close()
