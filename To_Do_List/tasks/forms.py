from . models import Task
from django import forms


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ('title', 'description', 'category')
        labels = {
            'title': 'Task Title',
            'description': 'Task Description',
            'category': 'Task Category',
        }