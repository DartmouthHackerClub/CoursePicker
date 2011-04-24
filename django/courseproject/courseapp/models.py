from django.db import models
from django.contrib import admin

class Profile(models.Model):
    key = models.CharField(max_length=60)
    favorites = models.ManyToManyField('Course')

class Course(models.Model):
    title = models.CharField(max_length=80, blank=True)
    professors = models.ManyToManyField('Professor', blank=True)
    dept = models.CharField(max_length=10, blank=True)      # TODO map to long name using some global mapping to long form
    number = models.IntegerField(blank=True, null=True)

    def rightpad_number(self):
        return '%-3s' % self.number

    def __unicode__(self):
        return '%s-%s' % (self.dept, self.number)

class CourseOffering(models.Model):
    course = models.ForeignKey('Course')
    distrib = models.ManyToManyField('Distrib', blank=True)

    term = models.CharField(max_length=5, blank=True)
    section = models.IntegerField(blank=True, null=True)
    
    crosslisted = models.ManyToManyField('CourseOffering', blank=True)

    crn = models.IntegerField(blank=True, null=True)
    cap = models.IntegerField(blank=True, null=True)
    enrollment = models.IntegerField(blank=True, null=True)
    location = models.CharField(max_length=70, blank=True)
    lab = models.NullBooleanField(blank=True, null=True)
    nro = models.NullBooleanField(blank=True, null=True)
    seminar = models.NullBooleanField(blank=True, null=True)
    examdate = models.DateField(blank=True, null=True)
    median = models.CharField(max_length=10, blank=True) 

    def __unicode__(self):
        return '%s-%s-%s-%s' % (self.term, self.course.dept, self.course.number, self.section)

    def rightpad_section(self):
        return '%-3s' % self.section

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

admin.site.register(Profile)
admin.site.register(Course)
admin.site.register(CourseOffering)
admin.site.register(Professor)
admin.site.register(Review)
admin.site.register(Distrib)
