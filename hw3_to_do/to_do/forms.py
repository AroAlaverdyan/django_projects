from django.forms import ModelForm
from django import forms
from .models import NewToDo


class TaskForm(ModelForm):
	
	class Meta:
		model = NewToDo
		fields = '__all__'
		exclude = ['user']

