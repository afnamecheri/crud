from django.shortcuts import render,HttpResponse
from .models import Students
from .forms import StudentForm

def add_students(request):
    print(request)
    frm=StudentForm()
    if request.POST:
        frm=StudentForm(request.POST)
        if frm.is_valid():
            frm.save()
        else:
            frm=StudentForm()
    return render(request,"add.html",{'frm':frm})

def list_students(request):
    students_list=Students.objects.all()
    response=render(request,"list.html",{"students":students_list})
    return response

def update_students(request,pk):
    student=Students.objects.get(pk=pk)
    if request.POST:
        frm=StudentForm(request.POST,instance=student)
        if frm.is_valid():
            student.save()
    else:
            frm=StudentForm(instance=student)

    return render(request,"add.html",{'frm':frm})

def delete_students(request,pk):
    student=Students.objects.get(pk=pk)
    student.delete()
    students_list=Students.objects.all()
    return render(request,"list.html",{'students':students_list})
