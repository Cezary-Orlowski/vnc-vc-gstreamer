import pika, os
import mysql.connector

connectMySQL = mysql.connector.connect(user='root', password='test', host='mysql', database='joomla')
cursor = connectMySQL.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS weather (`temp` float(30));")

url = os.environ.get('rabbitmq', 'amqp://guest:guest@rabbitmq/%2f')
params = pika.URLParameters(url)
params.socket_timeout = 5
connection = pika.BlockingConnection(params)
channel = connection.channel()
def callback(ch, method, preporties, body):
	print(" Received %r "% body)
	cursor.execute("""INSERT INTO weather (temp) VALUES ((%f))"""  % (float(body)))
	connectMySQL.commit()

channel.basic_consume(queue='data_queue', on_message_callback=callback, auto_ack=True)

print("Waiting for messages")
channel.start_consuming()
