from django.db import models

class Student(models.Model):
    forename = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)

    def __str__(self):
        return "{} {}".format(self.lastname, self.forename)

class Lehrveranstaltung(models.Model):
    bezeichnung = models.CharField(max_length=50)
    teilnehmer = models.ManyToManyField(Student, blank=True)

    def __str__(self):
        return self.bezeichnung
    




