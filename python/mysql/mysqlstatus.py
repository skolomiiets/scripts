#!/usr/bin/python
#importing modules
import MySQLdb, ConfigParser, os, time

#parsing configfile for credentials
config = ConfigParser.ConfigParser()
config.read("myconfig")
my_username = config.get('mysql', 'user')
my_password = config.get('mysql', 'password')
my_hostname = config.get('mysql', 'host')
my_port = config.get('mysql', 'port')
#print hostname, port, username, password

#connecting to mysql
if my_port > 0:
    db = MySQLdb.connect(host = my_hostname, user = my_username, passwd = my_password, port = int(my_port))
else:
    db = MySQLdb.connect(host = my_hostname, user = my_username, passwd = my_password)
while 1:
    os.system('clear')
    c=db.cursor()
    c.execute('SHOW FULL PROCESSLIST')
#    print c.fetchone()
#    for row in c.fetchall():
#	print row[0], " ", row[1]
