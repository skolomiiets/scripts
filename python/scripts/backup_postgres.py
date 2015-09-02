#!/usr/bin/env python
#this script creates gzip arkiv of postgresql database
import ConfigParser, os, time, sys
try:
    sys.argv[1], sys.argv[2]
except:
    sys.exit("Usage of this script: " + sys.argv[0] + " database path_to_location_gzipped_backup")
data = time.strftime("%d%m-%H_%M") # this is a timestamp
db = sys.argv[1]
path = sys.argv[2] + '/'
#parsing configfile for credentials
config = ConfigParser.ConfigParser()
config.read("/backup/postgres.cnf")
p_username = config.get('backups', 'user')
p_password = config.get('backups', 'password')
p_hostname = config.get('backups', 'host')
p_port = config.get('backups', 'port')
os.putenv('PGPASSWORD', p_password)
#print p_username, p_password, p_hostname, p_port
#script = os.system('pg_dump -h127.0.0.1 -Ubackup yachad | gzip >' + data + 'pgdump.zip')
execution = 'pg_dump -h127.0.0.1 -Ubackup %s | gzip > %s%s_%s.gzip' % (db, path, data, db)
script = os.system(execution)
script
