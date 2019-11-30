from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST

from .models import Task
from .forms import TaskForm


def index(request):
    task_list = Task.objects.order_by('id')

    form = TaskForm()

    context = {'task_list': task_list, 'form': form}

    return render(request, 'tasks/index.html', context)


@require_POST
def addTask(request):
    form = TaskForm(request.POST)

    if form.is_valid():
        new_task = Task(text=request.POST['text'])
        new_task.save()

    return redirect('index')


def completeTask(request, task_id):
    task = Task.objects.get(pk=task_id)
    task.done = True
    task.save()

    return redirect('index')

def deleteCompleted(request):
    Task.objects.filter(done__exact=True).delete()

    return redirect('index')

def deleteAll(request):
    Task.objects.all().delete()

    return redirect('index')

