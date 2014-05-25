from xml.etree.ElementTree import ElementTree
from sys import argv
from datetime import datetime
import time
import json
import psycopg2
import os, sys

tree = ElementTree()
conn = psycopg2.connect(database="dbturnrestriction", user="postgres",password="1234")
cursor = conn.cursor()

if (len(argv) < 2):
    print "ingrese archivo"
    exit()

tree.parse(argv[1])
for w in tree.iterfind('relation'):
	name = ''
	restriction = ''
	type = ''
	tags = {}
	for t in w.iterfind('tag'):
		tags[t.attrib['k']] = t.attrib['v']
		if tags.has_key('restriction'):
		 	restriction = tags['restriction']
		if tags.has_key('type'):
		 	type = tags['type']
		if tags.has_key('name'):
		 	name = tags['name']

	osm_timestamp = time.mktime(datetime.strptime(w.attrib['timestamp'], '%Y-%m-%dT%H:%M:%SZ').utctimetuple())
	id = w.attrib['id']
	uid = w.attrib['uid']
	osm_user = w.attrib['user']
	version = int(w.attrib['version'])
	changeset = w.attrib['changeset']
	query = "INSERT INTO relation(id, uid, osm_user, version, changeset, osm_timestamp, name, restriction, type)  VALUES  (%s, %s, %s, %s, %s, %s, %s, %s, %s);"
	cursor.execute(query, (id, uid, osm_user, version, changeset, osm_timestamp,name, restriction, type))
	print query

cursor.close()
conn.commit()
conn.close()
print 'saving on db'



