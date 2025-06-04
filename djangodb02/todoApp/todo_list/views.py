from django.shortcuts import render
from .models import todo
from .forms import TodoForm

def home(request):
    if request.method == 'POST':
        form = TodoForm(request.POST or None)
        if form.is_valid():
            form.save()
            return render(request, 'home.html', {'todos':todos})
    else:
        todos = todo.object.all()
        return render(request, 'home.html', {'todos' : todos})

def about(request):
    context = {'name': 'Gustavo', 'age': 20}
    return render(request, 'about.html', context)