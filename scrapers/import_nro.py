#!/usr/bin/python

# takes json from stdin and loads into nro table

import couchdb
import sys
import json

couch = couchdb.Server()

if 'nro' in couch:
    del couch['nro']
db = couch.create('nro')

nro_data = json.loads(sys.stdin.readline())

print nro_data

print 'Populating NRO records'

db.update(nro_data)
