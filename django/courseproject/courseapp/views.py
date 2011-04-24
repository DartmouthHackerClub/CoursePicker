from models import CourseOffering
from models import Course
from models import Distrib
from models import Professor

def populate_medians(request):
    import medians
    records = medians.load()

    for record in records:
        # medians correspond to offerings

        # Course
        c = Course.objects.get_or_create(dept=record['dept'], number=record['number'])
        c.dept = record['dept']
        c.number = record['number']
        c.put()

        # Course offering
        o = CourseOffering.objects.get_or_create(course=c, term=record['term'], section=record['section'])

        o.median = record['median']
        o.term = record['term']
        o.section = record['section']
        o.enrollment = record['enrollment']

        o.course = c
        o.put()
