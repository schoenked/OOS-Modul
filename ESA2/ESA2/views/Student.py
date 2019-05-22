from django.shortcuts import render
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse
from ESA2.models import Student
from ESA2.forms.student import StudentForm

def get_student_list(request):
    students=Student.objects.all().order_by('lastname')
    return render(request, 'student_list.html', {'page_title':'Studenten', 'students':students})

def add_student(request):
    student = Student()

    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            messages.success(request, 'Student gespeichert.')
            return HttpResponseRedirect(reverse('studentList'))
        else:
            messages.error(request, 'Speichern konnte nicht durchgeführt werden..')
    else:
        form = StudentForm(instance=student)

    return render(request, 'student.html', {'page_title':'Student hinzufügen', 'form':form})
