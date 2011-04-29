#!/bin/bash
tmpfile="/tmp/$(basename $0).$$.tmp"
DB=$1
CSV=$2
touch  $tmpfile
./timetable.pl < $CSV > $tmpfile
curl -X DELETE $1
sleep 0.2
curl -X PUT $1
curl  -H "Content-Type: application/json"  -d @$tmpfile -X POST $1_bulk_docs 
rm $tmpfile