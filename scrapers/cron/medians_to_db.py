#!/usr/bin/env python
# 
# Imports median json information to database
#

import couchdb
import medians

saveme = medians.load()

# insert into couch db
couch = couchdb.Server()
if not 'medians' in couch:
    couch.create('medians')
db = couch['medians']

if 'latest' in db:
    # delete old doc
    db.delete(db['latest'])
db['latest'] = saveme
