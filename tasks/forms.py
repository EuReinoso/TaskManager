from django import forms
from .models import Task, Block

class TaskForm(forms.ModelForm):

    class Meta:
        model = Task
        fields = ('description',)

class BlockForm(forms.ModelForm):

    class Meta:
        model = Block
        fields = ('title',)
