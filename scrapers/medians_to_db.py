#!/usr/bin/env python
# 
# Imports median json information to database
#

import couchdb
import medians

saveme = medians.load()

# insert into couch db
couch = couchdb.Server()
try:
    db = couch['medians']
except:
    couch.create('medians')
    db = couch['medians']

if db.get('latest'):
    # delete old doc
    db.delete(db['latest'])
db['latest'] = saveme
