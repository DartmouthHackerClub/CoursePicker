#!/usr/bin/env python
#
# Takes html containing medians table in, spits out JSON
#
# This format only works for medians 10W and on, about 2300 medians as of 11S.
# But it looks like the registrar standardized how they published medians.
#

import sys
import re
import urllib
import json

data = sys.stdin.read()

# Find links to individual median pages
urls = re.findall(r"http://www\.dartmouth\.edu/~reg/courses/medians/.*?\.html", data)

if not urls:
    print "Couldn't urls any median pages in input"
    sys.exit(1)

for url in urls:
    # Load median page and parse
    data = urllib.urlopen(url).read()
    rows = re.findall(r'\<tr align\=\"center\"\>[\s\n]*\<td\>(.+)?\<\/td\>[\s\n]*\<td\>(.+)?-(\d+)-(\d+)[\s\n]*\<\/td\>[\s\n]*\<td\>[\s\n]*(\d+)[\s\n]*\<\/td\>[\s\n]*\<td\>(.+)?\<\/td\>[\s\n]*', data)

    if rows:
        l = []
        for row in rows:
            clean_row = [x.strip() for x in row]
            d = {}
            d['term'] = clean_row[0]
            d['dept'] = clean_row[1]
            d['number'] = clean_row[2]
            d['section'] = clean_row[3]
            d['enrollment'] = clean_row[4]
            d['median'] = clean_row[5]
            l.append(d)

        print json.dumps(l)
