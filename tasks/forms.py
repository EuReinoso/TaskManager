from django import forms
from django.core.exceptions import ValidationError
from .models import Task, Block
from django.contrib.auth import get_user_model

class TaskForm(forms.ModelForm):
    description = forms.CharField( max_length=1000,
                                   widget=forms.TextInput(attrs={ 'class' : 'form-control form-control-sm',
                                                                  'placeholder' : 'Add task...'}))
    class Meta:
        model = Task
        fields = ('description',)

class BlockForm(forms.ModelForm):
    title = forms.CharField( max_length=50,
                             widget=forms.TextInput(attrs={ 'class' : 'form-control form-control add-block-form',
                                                                  'placeholder' : 'New block...'}))

    class Meta:
        model = Block
        fields = ('title',)

class UserForm(forms.Form):
    username = forms.CharField( max_length=30, 
                                widget= forms.TextInput(attrs={ 'class' : 'form-control form-control-sm',
                                                                'placeholder' : 'Add user...'}))

    def clean_username(self):
        username = self.cleaned_data['username']

        try:
            get_user_model().objects.get(username=username)
        except:
            raise ValidationError('Username not found.')


        
