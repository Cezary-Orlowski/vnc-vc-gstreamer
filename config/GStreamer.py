import os, psycopg2, sys

def convertToBinaryData(filename):
	with open(filename, 'rb') as file:
    	binaryData = file.read()
	return binaryData
       	 
os.system("mkdir /home/user/Desktop/images")
os.system("gst-launch-1.0 filesrc location=/home/user/Desktop/Clock.mp4 ! decodebin ! videoconvert ! pngenc ! multifilesink location=/home/user/Desktop/images/%d.png")
conn = psycopg2.connect(host="postgres", database="joomla", user="root", password="test")
cursor = conn.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS images (photo BYTEA NOT NULL)")
conn.commit()
data = convertToBinaryData("/home/user/Desktop/images/2.png")
cursor.execute("INSERT INTO images(photo) VALUES (%s)", (data,) )
conn.commit()
if conn:
	conn.close()
	os.system("rm -rf /home/user/Desktop/images")
