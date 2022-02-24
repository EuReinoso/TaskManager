from django import forms
from django.core.exceptions import ValidationError
from .models import Task, Block
from django.contrib.auth import get_user_model

class TaskForm(forms.ModelForm):

    class Meta:
        model = Task
        fields = ('description',)

class BlockForm(forms.ModelForm):

    class Meta:
        model = Block
        fields = ('title',)

class UserForm(forms.Form):
    username = forms.CharField(max_length=30)

    def clean_username(self):
        username = self.cleaned_data['username']

        try:
            get_user_model().objects.get(username=username)
        except:
            raise ValidationError('Username not found.')


        
