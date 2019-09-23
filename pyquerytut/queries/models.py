from django.db import models


class Organization(models.Model):
    name = models.CharField(max_length=50)


class Instructor(models.Model):
    name = models.CharField(max_length=50)
    employer = models.ForeignKey(Organization, on_delete=models.CASCADE)


class Course(models.Model):
    name = models.CharField(max_length=50)
    instructors = models.ManyToManyField(Instructor)
    organizations = models.ManyToManyField(Organization)
