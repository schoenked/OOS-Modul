from django.forms import ModelForm
from ESA2.models import Lehrveranstaltung

class LehrveranstaltungForm(ModelForm):
    class Meta:
        model = Lehrveranstaltung
        fields = "__all__" 
        labels = {
            'bezeichnung' : 'Bezeichnung',
        }