from django.shortcuts import render

from .models import Task, Block

def tasks(request):
    blocks = Block.objects.all()
    tasks = Task.objects.all()
    return render(request, 'tasks/index.html', {'blocks' : blocks, 'tasks' : tasks})