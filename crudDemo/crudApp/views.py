from django.shortcuts import render, redirect
from crudApp.models import Student
from crudApp.form import StudentForm
# Create your views here.

def retrive(request):
    students=Student.objects.all().values()
    context={
        'students':students
    }
    return render(request,'crudapp/index.html',context=context)


def add_info(request):
    form=StudentForm()
    if request.method=='POST':
        form= StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect ('/retrive')

    return render( request, 'crudapp/create.html',{'form':form})


def delete (request,id):
    student=Student.objects.get(id=id)
    student.delete()
    return redirect ('/retrive')

def update (request,id):
    student=Student.objects.get(id=id)
    if request.method=='POST':
        form= StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect ('/retrive')
    return render(request,'crudapp/update.html',{'student':student})