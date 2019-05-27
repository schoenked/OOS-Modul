from django.shortcuts import render,get_object_or_404
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse
from ESA2.forms.einschreiben import EinschreibungForm

def einschreiben_form(request):
    
    if request.method == 'POST':
        form = EinschreibungForm(request.POST)
        if form.is_valid():
            #einschreiben
            lv = form.cleaned_data['lv']
            lv.teilnehmer.add(form.cleaned_data['student'])
            #speichern
            lv.save()            
            messages.success(request, 'Student eingeschrieben.')
            return HttpResponseRedirect(reverse('home'))
        else:
            messages.error(request, 'Falsche Eingabe.')
    else:
        page_title = 'Student einschreiben'
        form = EinschreibungForm()
        return render(request, 'einschreiben.html', {'page_title':page_title, 'form':form})
