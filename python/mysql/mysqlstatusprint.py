#!/usr/bin/python
#importing modules
import MySQLdb, ConfigParser, os, time, curses, texttable

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
#os.system('clear')
while 1:
    time.sleep(1)
    os.system('clear')
    tab = texttable.Texttable()
    x = [[]]
    c=db.cursor()
    c.execute('SHOW FULL PROCESSLIST')
#    print c.fetchone(),
#    print c.fetchall()
    for row in c.fetchall():
	x.append()
    tab.addrows(x)
    tab.set_cols_align(['r'])
    tab.header(['0'], ['1']['2']['3']['4']['5']['6']['7'])
    print tab.draw()
