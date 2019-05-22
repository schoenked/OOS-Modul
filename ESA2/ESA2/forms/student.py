from django.forms import ModelForm
from ESA2.models import Student

class StudentForm(ModelForm):
    class Meta:
        model = Student
        fields = "__all__" 
        labels = {
            'forename' : 'Vorname',
            'lastname' : 'Nachname',
        }