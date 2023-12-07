from django.shortcuts import render, redirect
from .forms import Add_Task
from .models import Task
# Create your views here.

def task(request):
    if request.method == 'POST':
        add_task = Add_Task(request.POST)
        if add_task.is_valid():
            add_task.save()
            return redirect('home_page')
    else:
        add_task = Add_Task()
    return render(request,'task.html',{'form':add_task})

def edit_task(request,id):
    edTask = Task.objects.get(pk=id)
    add_task = Add_Task(instance=edTask)
    if request.method == 'POST':
        add_task = Add_Task(request.POST, instance=edTask)
        if add_task.is_valid():
            add_task.save()
            return redirect('home_page')
    return render(request,'task.html',{'form':add_task})

def delete_task(request,id):
    edTask = Task.objects.get(pk=id)
    edTask.delete()
    return redirect('home_page')
