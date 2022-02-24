from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model

from .models import Task, Block
from .forms import BlockForm, TaskForm, UserForm


# VIEWS ---------------------------------------------------------------------------------------------------------

@login_required
def tasks(request, data = None):
    blocks = Block.objects.filter(user= request.user).order_by('updated_at')    
    doingtasks = Task.objects.filter(done= 'doing')
    donetasks = Task.objects.filter(done= 'done')
    task_form = TaskForm()
    block_form = BlockForm()
    user_form = UserForm()

    
    if request.method == 'POST':
            if 'add-block-button' in request.POST:
                add_block(request)
    
    args = {'blocks' : blocks,
            'doingtasks' : doingtasks, 
            'donetasks' : donetasks, 
            'task_form' : task_form, 
            'block_form' : block_form,
            'user_form' : user_form,
            }

    if data != None:
        args.update(data)
    
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

@login_required
def add_task(request, id):
    block = get_object_or_404(Block, pk= id)
    task_form = TaskForm(request.POST)

    if task_form.is_valid():
        task = task_form.save(commit= False)
        task.done = 'doing'
        task.block = block
        task_form.save()

    return redirect('/')

@login_required
def add_user(request, id):
    block = get_object_or_404(Block, pk=id)
    
    print(request.POST)
    user_form = UserForm(request.POST)
    if user_form.is_valid():
        username = user_form.data['username']
        print(username)
        user = get_user_model().objects.get(username=username)
        block.user.add(user)
    else:
        return render(request, 'tasks/usernotfound.html', context= {'user_form' : user_form})

    return redirect('/')

def del_user(request, user_id, block_id):
    print("USER {} DELETED".format(user_id))
    user = get_object_or_404(get_user_model(), pk=user_id)
    block= get_object_or_404(Block, pk=block_id)

    block.user.remove(user)

    return redirect('/')

# FUNCTIONS ----------------------------------------------------------------------------------------------------

def add_block(request):
    form = BlockForm(request.POST)
    if form.is_valid():
        block = form.save(commit=False)
        block.owner = request.user
        block.save()
        block.user.add(request.user) #add a user to the owner

    return redirect('/')
