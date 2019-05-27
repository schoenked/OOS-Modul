from django.forms import Form
from django import forms
from ESA2.models import Lehrveranstaltung
from ESA2.models import Student

class EinschreibungForm(Form):
    lv = forms.ModelChoiceField(queryset=Lehrveranstaltung.objects.all(), required=True, empty_label='Lehrveranstaltung wählen', label='Lehrveranstaltung wählen')
    student = forms.ModelChoiceField(queryset=Student.objects.all(), required=True, empty_label='Student wählen', label='Student wählen')
