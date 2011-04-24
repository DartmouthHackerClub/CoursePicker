from django.db import models
from django.contrib import admin

class User(models.Model):
    key = models.CharField(max_length=60)
    favorites = models.ManyToManyField('Course')

class Course(models.Model):
    key = models.CharField(max_length=60)
    professors = models.ManyToManyField('Professor')

class CourseOffering(models.Model):
    course = models.ForeignKey('Course')
    distrib = models.ManyToManyField('Distrib')

    dept = models.ManyToManyField('Department')
    term = models.CharField(max_length=5)
    number = models.IntegerField()
    section = models.IntegerField()

    crn = models.IntegerField()
    cap = models.IntegerField()
    location = models.CharField(max_length=70)
    lab = models.BooleanField()
    nro = models.BooleanField()
    seminar = models.BooleanField()
    examdate = models.DateField()
    median = models.CharField(max_length=10)

class Department(models.Model):
    short = models.CharField(max_length=10)

    def long(self):
        # map to long name using some global mapping to long form
        pass

class Professor(models.Model):
    key = models.CharField(max_length=60)
    name = models.CharField(max_length=60)
    text = models.TextField()

class Review(models.Model):
    course_offering = models.ForeignKey('CourseOffering')
    title = models.CharField(max_length=60)
    text = models.TextField()

class Distrib(models.Model):
    name = models.CharField(max_length=60)

admin.site.register(User)
admin.site.register(Course)
admin.site.register(CourseOffering)
admin.site.register(Professor)
admin.site.register(Review)
admin.site.register(Distrib)
admin.site.register(Department)
