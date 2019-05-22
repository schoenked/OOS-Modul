from django.shortcuts import render

def as_View(request):
    return render(request, 'home.html', {'page_title':'Studentenverwaltung'})