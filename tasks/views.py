from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from django import forms

from .models import Task, Block
from .forms import BlockForm, TaskForm


# VIEWS ---------------------------------------------------------------------------------------------------------

@login_required
def tasks(request):
    blocks = Block.objects.all().order_by('-created_at').filter(user=request.user)
    doingtasks = Task.objects.filter(done= 'doing')
    donetasks = Task.objects.filter(done= 'done')
    task_form = TaskForm()
    block_form = BlockForm()

    
    if request.method == 'POST':
            if 'add-block-button' in request.POST:
                add_block(request)
            else:
                add_task(request, blocks)
    
    args = {'blocks' : blocks, 'doingtasks' : doingtasks, 'donetasks' : donetasks, 'task_form' : task_form, 'block_form' : block_form}
    return render(request, 'tasks/index.html', args)

@login_required
def change_task_status(request, id):
    task = get_object_or_404(Task, pk=id)
    
    if task.done == 'doing':
        task.done = 'done'
    else:
        task.done = 'doing'

    task.save()

    return redirect('/')

@login_required
def del_task(request, id):
    task = get_object_or_404(Task, pk=id)
    task.delete()

    return redirect('/')

@login_required
def del_block(request, id):
    block = get_object_or_404(Block,pk=id)
    block.delete()

    return redirect('/')

# FUNCTIONS ----------------------------------------------------------------------------------------------------

def add_block(request):
    form = BlockForm(request.POST)
    if form.is_valid():
        block = form.save(commit=False)
        block.user = request.user
        block.save()

    return redirect('/')

def add_task(request, blocks):
    task_form = TaskForm(request.POST)
    if task_form.is_valid():
        task = task_form.save(commit=False)
        task.done = 'doing'

        block_id = 0
        for block in blocks:
            if 'add-task-button-' + str(block.id) in request.POST:
                block_id = block.id

                task.block = Block.objects.get(id= block_id)
                task_form.save()

    return redirect('/')