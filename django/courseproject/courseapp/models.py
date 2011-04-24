from django.db import models

class User(models.Model):
    id = models.CharField()

class Course(models.Model):
    id = models.CharField()
    professors = models.ManyToManyField('Professor')

class CourseOffering(models.Model):
    course = models.ForeignKey('Course')
    distrib = models.ManyToManyField('Distrib')
    term = models.ForeignKey('Term')

    cap = models.IntegerField()
    location = models.CharField()
    lab = models.BooleanField()
    nro = models.BooleanField()
    seminar = models.BooleanField()
    examdate = models.DateField()

class Term(models.Model):
    id = models.CharField()

class Professor(models.Model):
    id = models.CharField()
    name = models.CharField()
    text = models.TextField()

class Review(models.Model):
    title = models.CharField()
    text = models.TextField()

class Distrib(models.Model):
    name = models.CharField()
