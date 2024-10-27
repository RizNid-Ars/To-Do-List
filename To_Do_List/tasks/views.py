from django.shortcuts import render
from . models import Task
from tasks.forms import TaskForm
from django.shortcuts import redirect

def base_view(request):
    return render(request, 'base.html')


def task_list_view(request):
    tasks = Task.objects.all()
    return render(request, 'task_list.html', {'tasks': tasks})


def task_detail_view(request, id):
    task = Task.objects.get(id=id)
    return render(request, 'task_detail.html', {'task': task})


def task_create_view(request):
    if request.method == 'GET':
        form = TaskForm()
        return render(request, 'task_create.html', {'form': form})
    if request.method == 'POST':
        form = TaskForm(request.POST, request.FILES)
        post = form.save()
        post.user = request.user
        post.save()
        return redirect('/tasks/')