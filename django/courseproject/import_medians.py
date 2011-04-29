#!/usr/bin/env python

from django.conf import settings
from courseapp.models import CourseOffering
from courseapp.models import Course
import medians

def go():
    records = medians.load()

    for record in records:
        # medians correspond to offerings
        print record

        # Course
        c,created = Course.objects.get_or_create(dept=record['dept'], number=record['number'])
        if created:
            c.dept = record['dept']
            c.number = record['number']
            c.save()

        # Course offering
        o,created = CourseOffering.objects.get_or_create(course=c, term=record['term'], section=record['section'])

        o.median = record['median']
        if created:
            o.term = record['term']
            o.section = record['section']
            o.enrollment = record['enrollment']
            o.course = c

        o.save()

if __name__ == "__main__":
    go()
