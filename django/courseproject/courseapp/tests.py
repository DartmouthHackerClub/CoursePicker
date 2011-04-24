from django.test import TestCase
from models import *

class SimpleTest(TestCase):
    def setUp(self):
        c1 = Course(title='THE COOL COURSE')
        p1 = Professor(name="Julie Ming")
        c1.pro
        c1.save()

    def test_basic_addition(self):
        """
        Tests that 1 + 1 always equals 2.
        """
        self.assertEqual(1 + 1, 2)
