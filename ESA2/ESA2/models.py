from django.db import models

class student(django.models):
    forename=models.CharField(max_length=50)
    lastname=models.CharField(max_length=50)

class lehrveranstaltung(django.models):
    name=models.CharField(max_length=50)




