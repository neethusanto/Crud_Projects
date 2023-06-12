from django.shortcuts import render,redirect,get_object_or_404
from  django.http import HttpResponse
from .models import Task
from .forms import CrudForm
# Create your views here.
def home (request):
    task1=Task.objects.all()
    if request.method=='POST':
        slno=request.POST.get('slno','')
        name=request.POST.get('itemname','')
        description=request.POST.get('description','')
        task=Task(slno=slno,name=name,description=description)
        task.save()
    return render(request,'home.html',{'task1':task1})

def delete(request,crudtaskid):
    task=Task.objects.get(id=crudtaskid)
    if request.method=='POST':
        task.delete()
        return redirect('/')
    return render(request,'delete.html') 


def update(request,id):
    task=get_object_or_404(Task,id=id)
    if request.method=='POST':
        task.slno=request.POST.get('slno')
        task.name=request.POST.get('itemname')
        task.description=request.POST.get('description')
        task.save()
        return redirect('/')
    return render(request,'update.html',{'task':task})   