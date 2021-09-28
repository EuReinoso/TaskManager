from django.shortcuts import redirect, render

from .models import Task, Block
from .forms import TaskForm

def tasks(request):
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

            task.block = Block.objects.get(title=block_title)
            form.save()
            return redirect('/')

    else:
        return render(request, 'tasks/index.html', {'blocks' : blocks, 'tasks' : tasks, 'form' : form})