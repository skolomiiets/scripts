#!/usr/bin/python
#importing modules
import MySQLdb

#parsing configfile for credentials
storage = open('myconfig')
for lines in storage:
    if 'host' in lines:	
	my_host = lines.split(' ')[-1]
    elif 'port' in lines:
	my_port = lines.split(' ')[-1]
    elif 'user' in lines:
	my_user = lines.split(' ')[-1]
    elif 'password' in lines:
	my_password = lines.split(' ')[-1]
#print host, port, user, password

#connecting to mysql
db = MySQLdb.connect(host=my_host,port=my_port,user=my_user,passwd=my_password)
c=db.cursor()
c.execute('SHOW FULL PROCESSLIST')
c.fetchchone()
