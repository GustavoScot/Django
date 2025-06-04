from django import forms
from .models import todo

class TodoForm(forms.ModelForm):

    class meta:
        model = todo
        fields = ['title', 'isCompleted']