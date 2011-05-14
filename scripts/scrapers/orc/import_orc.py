#!/usr/bin/python

# takes json from stdin and loads into orc table

import couchdb
import sys
import json
from couchdb.schema import Document

couch = couchdb.Server()

orc_data = json.loads(sys.stdin.readline())

courses = couch['courses']

# only need to run this once
for course_id in courses:
    course = courses[course_id]
    course['description'] = 'true'
    course['meets'] = 'true'
    courses[course_id] = course

sys.exit(1)

def dept_query(dept):
    return "function(doc) {\
    for (var i in doc.names)\
        if (doc.names[i].Department == '%s')\
          emit(doc._id, doc);}" % dept

def course_query(dept, num):
    return "function(doc) {\
    for (var i in doc.names)\
        if (doc.names[i].Department == '%s' && doc.names[i].Number == '%03d')\
          emit(doc._id, doc);}" % (dept, num)


for no_orc in orc_data:
    dept = no_orc['department']
    nums = no_orc['courses']
#    print dept, nums
    if nums == 'all':
        query_func = dept_query(dept)
#        print query_func
        for row in courses.query(query_func):
#            print row.key, row.value
            row.value['orc'] = 'false'
            courses[row.key] = row.value
#            print courses[row.key]
        
    else:
        for num in nums:
            query_func = course_query(dept, num)
#            print query_func
            for row in courses.query(query_func):
#                print row.key, row.value
                row.value['orc'] = 'false'
                courses[row.key] = row.value
#                print courses[row.key]
