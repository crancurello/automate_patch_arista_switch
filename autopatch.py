#!/usr/bin/python

from Exscript.protocols import SSH2
from Exscript import Account
from time import sleep
import csv
import re

"""
# OPCION CON UN SOLO HOST. LA IP DE ESTA DECLARADA EN LA VARIABLE IP

ip='192.168.1.1'
username='##USERNAME##'
password='##PASSWORD##'

account = Account(username,password)
conn = SSH2()

conn.connect('%s' % ip)
conn.login(account)
conn.execute('copy ftp://ftpserver.local/secAdvisory0015.swix flash:')
sleep(1)
conn.execute('copy flash:secAdvisory0015.swix extension:')
sleep(1)
conn.execute('extension secAdvisory0015.swix')
sleep(1)
conn.execute('copy installed-extensions boot-extensions')
sleep(1)
conn.execute('delete secAdvisory0015.swix')
conn.send('exit\r')
conn.close()
"""

# OPCION IMPORTANDO LOS HOSTS DESDE UN CSV LLAMADO HOSTLIST

username='##USERNAME##'
password='##PASSWORD##'

with open('hostlist.csv', 'rb') as f:
    reader=csv.reader(f)
    host_temp_list=list(reader)

account = Account(username,password)
conn = SSH2()

for host in host_temp_list:
	try:
		print "se comienza a ejecutar en el host ", repr(host[0])
		conn.connect('%s'%host[0])
		conn.login(account)
		conn.execute('copy ftp://ftpserver.local/secAdvisory0015.swix flash:')
		sleep(2)
		conn.execute('copy flash:secAdvisory0015.swix extension:')
		sleep(1)
		conn.execute('extension secAdvisory0015.swix')
		sleep(1)
		conn.execute('copy installed-extensions boot-extensions')
		sleep(1)
		conn.execute('delete secAdvisory0015.swix')
		print "se ejecuto correctamente todo el script en el host", repr(host[0])
		print ""
		conn.send('exit\r')
		conn.close()
	except:
		print "Algo fallo"