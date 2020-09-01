import pika, os, threading, random

def get_somenumber():
    randomnum = round(random.uniform(-30, 30), 1)
    return randomnum

def queue():
    threading.Timer(5.0, queue).start()
    url = os.environ.get('rabbitmq', 'amqp://guest:guest@rabbitmq/%2f')
    params = pika.URLParameters(url)
    params.socket_timeout = 5
    connection = pika.BlockingConnection(params)
    channel = connection.channel()
    channel.basic_publish(exchange='data_exchange', routing_key='data_queue', body=str(get_somenumber()))
    connection.close()
    
queue()