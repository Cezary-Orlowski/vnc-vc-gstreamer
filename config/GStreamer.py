import os, psycopg2, sys

def readImage(name):
    try:
        fin = open("%s.png", name, "rb")
        img = fin.read()
        return img

    except IOError, e:
        print "Error %d: %s" % (e.args[0],e.args[1])
        sys.exit(1)

    finally:
        if fin:
            fin.close()
try:
    i = 1
    os.system("mkdir /home/user/Desktop/images")
    os.system("gst-launch-1.0 filesrc location=/home/user/Desktop/Clock.mp4 ! decodebin ! videoconvert ! pngenc ! multifilesink location=/home/user/Desktop/images/%d.png")
    number = len(next(os.walk('/home/user/Desktop/images'))[2])
    for i <= number
        conn = psycopg2.connect(database = "joomla", user = "root", password = "test", host = "postgres", port = "5432")
        cursor = conn.cursor()
        cursor.execute("CREATE TABLE IF NOT EXISTS weather (`temp` float(30));")
        data = readImage(name)
        binary = psycopg2.Binary(data)
        cursor.execute("INSERT INTO images(data) VALUES (%s)", (binary,) )
        conn.commit()
        i += 1
except psycopg2.DatabaseError, e:
    if conn:
        conn.rollback()
    print 'Error %s' % e    
    sys.exit(1)
finally: 
    if conn:
        conn.close()
        os.system("rm -rf /home/user/Desktop/images")