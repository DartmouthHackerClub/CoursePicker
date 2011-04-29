from django.test import TestCase
from django.test.client import Client
from models import *

class SimpleTest(TestCase):
    def setUp(self):
        c1 = Course(title='Intro Computer Science', dept='COSC', number='5')
        c1.save()
        p1 = Professor(name="Julie Ming")
        p1.save()
        o1 = CourseOffering(course=c1)
        o1.save()
        o1.professors.add(p1)
        o1.save()

    def test_search(self):
        c = Client()
        search_data = {
            'professor' : 'Julie Ming',

        }
        response = c.post('/get_search/', search_data)
