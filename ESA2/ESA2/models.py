from django.db import models

class Student(models.Model):
    forename=models.CharField(max_length=50)
    lastname=models.CharField(max_length=50)

class Lehrveranstaltung(models.Model):
    name=models.CharField(max_length=50)




