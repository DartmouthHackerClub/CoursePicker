from django.db import models
from django.contrib import admin

class User(models.Model):
    key = models.CharField(max_length=60)

class Course(models.Model):
    key = models.CharField(max_length=60)
    professors = models.ManyToManyField('Professor')

class CourseOffering(models.Model):
    course = models.ForeignKey('Course')
    distrib = models.ManyToManyField('Distrib')
    term = models.ForeignKey('Term')

    crn = models.IntegerField()
    cap = models.IntegerField()
    location = models.CharField(max_length=70)
    lab = models.BooleanField()
    nro = models.BooleanField()
    seminar = models.BooleanField()
    examdate = models.DateField()

class Term(models.Model):
    key = models.CharField(max_length=5)

class Professor(models.Model):
    key = models.CharField(max_length=60)
    name = models.CharField(max_length=60)
    text = models.TextField()

class Review(models.Model):
    title = models.CharField(max_length=60)
    text = models.TextField()

class Distrib(models.Model):
    name = models.CharField(max_length=60)

admin.site.register(User)
admin.site.register(Course)
admin.site.register(CourseOffering)
admin.site.register(Term)
admin.site.register(Professor)
admin.site.register(Review)
admin.site.register(Distrib)
