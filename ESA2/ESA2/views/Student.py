from django.shortcuts import render
from ESA2.models import Student

def get_student_list(request):
    students=Student.objects.all().order_by('lastname')
    return render(request, 'student_list.html', {'page_title':'Studenten', 'students':students})