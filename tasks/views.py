from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render

from .models import Task, Block
from .forms import BlockForm, TaskForm


def tasks(request):
    blocks = Block.objects.all().order_by('-created_at')
    doingtasks = Task.objects.filter(done= 'doing')
    donetasks = Task.objects.filter(done= 'done')
    task_form = TaskForm()
    block_form = BlockForm()

    if request.method == 'POST':
        if 'add-block-button' in request.POST:
            form = BlockForm(request.POST)
            if form.is_valid():
                form.save()

            return redirect('/')
        else:
            task_form = TaskForm(request.POST)
            if task_form.is_valid():
                task = task_form.save(commit=False)
                task.done = 'doing'

                block_title = ''
                for block in blocks:
                    if 'add-task-button-' + block.title in request.POST:
                        block_title = block.title

                task.block = Block.objects.get(title= block_title)
                task_form.save()

            return redirect('/')
    
    args = {'blocks' : blocks, 'doingtasks' : doingtasks, 'donetasks' : donetasks, 'task_form' : task_form, 'block_form' : block_form}
    return render(request, 'tasks/index.html', args)

def change_task_status(request, id):
    task = get_object_or_404(Task, pk=id)
    
    if task.done == 'doing':
        task.done = 'done'
    else:
        task.done = 'doing'

    task.save()

    return redirect('/')


def del_task(request, id):
    task = get_object_or_404(Task, pk=id)
    task.delete()

    return redirect('/')

def del_block(request, id):
    block = get_object_or_404(Block,pk=id)
    block.delete()

    return redirect('/')


