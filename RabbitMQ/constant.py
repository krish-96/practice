from enum import Enum


class CommonProps(Enum):
    # default values
    DEFAULT_EXCHANGE = ''
    DEFAULT_EXCHANGE_TYPE = ''
    DEFAULT_QUEUE = ''
    # Exchanges
    SIMPLE_EXCHANGE = 'simple_exchange'
    WORK_QUEUES_EXCHANGE = 'work_queue_exchange'
    PUBSUB_EXCHANGE = 'pubsub_exchange'
    ROUTING_TOPIC_EXCHANGE = 'topic_exchange'
    ROUTING_DIRECT_EXCHANGE = 'direct_exchange'
    # Exchange Typess
    SIMPLE_EXCHANGE_TYPE = 'fanout'
    WORK_QUEUES_EXCHANGE_TYPE = 'fanout'
    PUBSUB_EXCHANGE_TYPE = 'fanout'
    ROUTING_TOPIC_EXCHANGE_TYPE = 'topic'
    ROUTING_DIRECT_EXCHANGE_TYPE = 'direct'
    # Queues
    SIMPLE_QUEUE = 'simple_queue'
    WORK_QUEUES_QUEUE = 'work_queue'
    PUBSUB_QUEUE = 'pubsub_queue'
    ROUTING_TOPIC_QUEUE = 'routing_topic_queue'
    ROUTING_DIRECT_QUEUE = 'routing_direct_queue'
