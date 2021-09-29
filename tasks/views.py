from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render

from .models import Task, Block
from .forms import TaskForm


def tasks(request, block_id=''):
    blocks = Block.objects.all()
    tasks = Task.objects.all()
    form = TaskForm()

    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.done = 'doing'

            block_title = ''
            for block in blocks:
                if block.title in request.POST:
                    block_title = block.title

            task.block = Block.objects.get(title= block_title)
            form.save()

            return redirect('/')


    args = {'blocks' : blocks, 'tasks' : tasks, 'form' : form}
    return render(request, 'tasks/index.html', args)

def del_task(request, id):
    task = get_object_or_404(Task, pk= id)
    task.delete()

    messages.info(request, 'Task Deleted')

    return redirect('/')


