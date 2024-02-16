import sys
import pika
import json
from datetime import datetime
from constant import CommonProps

database_data = {'first_name': "Gopi Krishna", "last_name": "Belamkonda", 'age': 27, "ssn": '12345'}
print("Message sent : %s" % database_data)
database_data = json.dumps(database_data)

PROPS = CommonProps


class RabbitMQProducer:
    """
    This class implements the use of RabbitMQ by using the module pika.
    This class will help to produce the messages and to send to the exchanger.
    We can also specify the queue name also.
    """
    __instance_exists = False

    def __new__(cls, *args, **kwargs):
        if not cls.__instance_exists:
            cls.__instance_exists = True
            return super(RabbitMQProducer, cls).__new__(cls)

        raise AttributeError(f"We cannot create an instance, as an instance already exists for RabbitMQProducer.")

    def __init__(self, method, sub_method=None, message=None):
        self.method = method
        self.sub_method = sub_method
        self.message = message
        if message is None:
            self.message = "Now the time is %s" % datetime.now().strftime('%Y-%m-%d %H:%M:%s')
        print("Message sent : %s" % self.message)

        self.connection = None
        self.channel = None
        self.exchange = ''
        self.content_type = 'application/json'
        self.delivery_mode = pika.DeliveryMode.Persistent

    def __enter__(self):
        print("Enter")
        connection_parameters = pika.ConnectionParameters('localhost')
        self.connection = pika.BlockingConnection(connection_parameters)
        self.channel = self.connection.channel()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Exit", "Connection is about to close!")
        self.connection.close()

    def trigger_the_function(self):
        trigger_method = "_%s" % method if method else '_default'
        trigger = getattr(self, trigger_method, self._default)
        print("GETATTR :", trigger)
        trigger()

    def on_msg_received(self, ch, method, properties, body):
        print("[-] Received Msg: %s " % body.decode())

    def start_consume(self):
        print("[x] Consumer is ready to consume : ")
        self.channel.start_consuming()

    def _default(self):
        print('DEFAULT')

    def _simple(self):
        print("SIMPLE")
        # simple_queue = self.channel.queue_declare(PROPS.SIMPLE_QUEUE.value, exclusive=True) # exclusive= True refers to automatic closing the queue
        simple_queue = self.channel.queue_declare(queue=PROPS.SIMPLE_QUEUE.value)
        self.channel.exchange_declare(PROPS.SIMPLE_EXCHANGE.value,
                                      exchange_type=PROPS.SIMPLE_EXCHANGE_TYPE.value)
        self.channel.queue_bind(exchange=PROPS.SIMPLE_EXCHANGE.value, queue=simple_queue.method.queue)
        self.channel.basic_consume(queue=simple_queue.method.queue, on_message_callback=self.on_msg_received)

    def _work_queues(self):
        print("WORK QUEUES")
        # self.channel.queue_declare(PROPS.WORK_QUEUES_QUEUE.value, exclusive=True) # exclusive= True refers to automatic closing the queue
        self.channel.queue_declare(PROPS.WORK_QUEUES_QUEUE.value)
        self.channel.basic_consume(queue=PROPS.WORK_QUEUES_QUEUE.value, on_message_callback=self.on_msg_received)

    def _pubsub(self):
        print("PUBSUB QUEUES")
        # self.channel.queue_declare(PROPS.PUBSUB_QUEUE.value, exclusive=True) # exclusive= True refers to automatic closing the queue
        pubsub_queue = self.channel.queue_declare(PROPS.PUBSUB_QUEUE.value)
        self.channel.exchange_declare(PROPS.PUBSUB_EXCHANGE.value,
                                      exchange_type=PROPS.PUBSUB_EXCHANGE_TYPE.value)
        self.channel.queue_bind(exchange=PROPS.PUBSUB_EXCHANGE.value, queue=pubsub_queue.method.queue)
        self.channel.basic_consume(queue=pubsub_queue.method.queue, on_message_callback=self.on_msg_received)

    def _routing(self):
        print("ROUTING")
        getattr(self, f"_{self.sub_method}", self._default)()

    def _direct(self):
        print("ROUTING DIRECT QUEUES")
        # self.channel.queue_declare(PROPS.ROUTING_DIRECT_QUEUE.value, exclusive=True) # exclusive= True refers to automatic closing the queue
        direct_queue = self.channel.queue_declare(PROPS.ROUTING_DIRECT_QUEUE.value)
        self.channel.exchange_declare(PROPS.ROUTING_DIRECT_EXCHANGE.value,
                                      exchange_type=PROPS.ROUTING_DIRECT_EXCHANGE_TYPE.value)
        self.channel.queue_bind(exchange=PROPS.ROUTING_DIRECT_EXCHANGE.value, queue=direct_queue.method.queue)
        self.channel.basic_consume(queue=direct_queue.method.queue, on_message_callback=self.on_msg_received)

    def _topic(self):
        print("ROUTING TOPIC QUEUES")
        # self.channel.queue_declare(PROPS.ROUTING_TOPIC_QUEUE.value, exclusive=True) # exclusive= True refers to automatic closing the queue
        direct_queue = self.channel.queue_declare(PROPS.ROUTING_TOPIC_QUEUE.value)
        self.channel.exchange_declare(PROPS.ROUTING_TOPIC_EXCHANGE.value,
                                      exchange_type=PROPS.ROUTING_TOPIC_EXCHANGE_TYPE.value)
        self.channel.queue_bind(exchange=PROPS.ROUTING_TOPIC_EXCHANGE.value, queue=direct_queue.method.queue)
        self.channel.basic_consume(queue=direct_queue.method.queue, on_message_callback=self.on_msg_received)


def verify_initials(method, sub_method):
    if method is None:
        print(">>> You must provide method!")
        exit(0)
    if method == 'routing' and sub_method is None:
        print(">>> You must provide sub method for the routing method!")
        exit(0)
    elif method == 'routing' and sub_method not in ('topic', 'direct'):
        print(">>> Provided invalid sub method under the routing method.")
        exit(0)
    return True


args = sys.argv
print("Args : %s" % args)

method = args[1] if len(args) >= 2 else None
sub_method = args[2] if len(args) > 2 else None

if verify_initials(method, sub_method):
    with RabbitMQProducer(method=method, sub_method=sub_method) as rmqp:
        rmqp.trigger_the_function()
        rmqp.start_consume()
