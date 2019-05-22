from django import forms
from django.forms import ModelForm
from ESA2.models import Student
from ESA2.models import Lehrveranstaltung

class StudentForm(ModelForm):
    class Meta:
        model = Student
        fields = "__all__" 
        
        lvs = forms.ModelMultipleChoiceField(queryset=Lehrveranstaltung.objects.filter())

        labels = {
            'forename' : 'Vorname',
            'lastname' : 'Nachname',
        }