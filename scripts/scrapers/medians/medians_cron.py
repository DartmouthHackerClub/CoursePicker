#!/usr/bin/env python
# 
# Imports median json information to database
#

import couchdb
import medians

COUCHDB_USER = 'mediancrawler'
COUCHDB_PASS = 'veQu6moh'

records = medians.load()

# Create database
couch = couchdb.Server()

if 'medians' in couch:
    del couch['medians']
db = couch.create('medians')

# Populate with a document per record
print 'Populating median records...'
db.update(records)
