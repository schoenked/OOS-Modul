from django.shortcuts import render,get_object_or_404
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse
from ESA2.models import Student
from ESA2.forms.student import StudentForm

def get_student_list(request):
    students=Student.objects.all().order_by('lastname')
    return render(request, 'student_list.html', {'page_title':'Studenten', 'students':students})

def student_form(request, pk=None):
    if pk==None:
        #create new
        student = Student()
        page_title='Student hinzufügen'

    else:
        #load
        student = get_object_or_404(Student,pk=pk)
        page_title='Student hinzufügen'

    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            messages.success(request, 'Student gespeichert.')
            return HttpResponseRedirect(reverse('studentList'))
        else:
            messages.error(request, 'Falsche Eingabe.')
    else:
        form = StudentForm(instance=student)

    return render(request, 'student.html', {'page_title':page_title, 'form':form})

def delete(request, pk=None):
    student = get_object_or_404(Student,pk=pk)
    if student==None:
        messages.error(request, 'Beim Löschen ist ein Fehler aufgetreten.')
    else:
        student.delete()
        messages.success(request, 'Student gelöscht.')
        return HttpResponseRedirect(reverse('studentList'))