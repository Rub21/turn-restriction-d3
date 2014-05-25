from xml.etree.ElementTree import ElementTree
from sys import argv
from datetime import datetime
import time
import json
import psycopg2
import os, sys


conn = psycopg2.connect(database="dbturnrestriction", user="postgres",password="1234")
cursor = conn.cursor()

#fecha de inicio
#s = argv[1] #"01/12/2011"
#print time.mktime(datetime.strptime(s, "%d/%m/%Y").timetuple())

#fecha actual
ts = int(time.time())
print ts

#timestamp_a_day = 86400;
day = '1'
s_year = ''
s_month = ''
for year in xrange(01, 14+1):
	for month in xrange(1,12+1):
		#print "%s/%d/20%d" %(day,month,year)
		if month < 10:
			s_month = "0%s" %(month)			
		else:
			s_month = "%s" %(month)

		s_date = "0%s/%s/20%d" %(day,s_month,year)

		print s_date
		ts_date = time.mktime(datetime.strptime(s_date, "%d/%m/%Y").timetuple())
		print ts_date
		query = "INSERT INTO fecha(s_date, ts_date) VALUES (%s, %s);"
		cursor.execute(query, (s_date, ts_date))
cursor.close()
conn.commit()
conn.close()
print 'saving on db'

