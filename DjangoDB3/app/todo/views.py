from django.shortcuts import render
from .models import Todo
from .forms import TodoForm

def home(request):
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
    todos = Todo.objects.all()
    return render(request, 'home.html', {'todos': todos})

def about(request):
    context = {
        'name': 'Gustavo', 
        'age': 21
        }
    return render(request, 'about.html', context)