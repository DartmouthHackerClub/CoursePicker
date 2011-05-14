#!/bin/sh
curl -XPUT 'http://hacktown.cs.dartmouth.edu:9200/medians/medians/_meta' -d '{
    "type" : "couchdb",
    "couchdb" : {
        "host" : "localhost",
        "port" : 5984,
        "db" : "medians",
        "filter" : null
    }
}'
