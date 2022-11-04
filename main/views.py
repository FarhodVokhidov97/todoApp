from django.shortcuts import render,redirect
from .models import Mytodo
from .forms import TodoForm
# Create your views here.

def alltodo(request):
    tasks = Mytodo.objects.all()
    form  = TodoForm()
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
    context = {
        'tasks':tasks,
        'form':form

    }
    return render(request,'alltodo.html',context)

def deleteTask(request,pk):
    task = Mytodo.objects.get(id=pk)
    task.delete()
    return redirect('alltodo')

def updateTask(request,pk):
    task = Mytodo.objects.get(id=pk)
    updateForm = TodoForm(instance=task)
    if request.method=='POST':
        updateForm = TodoForm(request.POST, instance= task)
        if updateForm.is_valid():
            updateForm.save()
            return redirect('alltodo')
    context={
        'task':task,
        'updateform':updateForm
    }
    return render(request,'update.html',context)