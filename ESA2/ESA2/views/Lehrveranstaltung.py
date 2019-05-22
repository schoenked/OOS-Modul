from django.shortcuts import render,get_object_or_404
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse
from ESA2.models import Lehrveranstaltung
from ESA2.forms.lehrveranstaltung import LehrveranstaltungForm

def get_lv_list(request):
    lvList=Lehrveranstaltung.objects.all().order_by('bezeichnung')
    return render(request, 'lv_list.html', {'page_title':'Lehrveranstaltungen', 'lehrveranstaltungen':lvList})

def lehrveranstaltung_form(request, pk=None):
    if pk==None:
        #create new
        lv = Lehrveranstaltung()
        page_title='Lehrveranstaltung hinzufügen'

    else:
        #load
        lv = get_object_or_404(Lehrveranstaltung,pk=pk)
        page_title='Lehrveranstaltung hinzufügen'

    if request.method == 'POST':
        form = LehrveranstaltungForm(request.POST, instance=lv)
        if form.is_valid():
            form.save()
            messages.success(request, 'Lehrveranstaltung gespeichert.')
            return HttpResponseRedirect(reverse('lvList'))
        else:
            messages.error(request, 'Falsche Eingabe.')
    else:
        form = LehrveranstaltungForm(instance=lv)

    return render(request, 'lv.html', {'page_title':page_title, 'form':form})

def delete(request, pk=None):
    lv = get_object_or_404(Lehrveranstaltung,pk=pk)
    if lv==None:
        messages.error(request, 'Beim Löschen ist ein Fehler aufgetreten.')
    else:
        lv.delete()
        messages.success(request, 'Lehrveranstaltung gelöscht.')
        return HttpResponseRedirect(reverse('lvList'))