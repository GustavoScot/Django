from django import forms
from .models import Todo

class TodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ['title', 'completed']
        labels = {
            'title': 'Título',
            'completed': 'Concluído',
        }