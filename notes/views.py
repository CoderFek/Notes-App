from django.shortcuts import render, redirect, get_object_or_404
from .models import Notes
from django.views.generic import ListView
from .forms import NotesForm
# Create your views here.

class Homeview(ListView):
    model = Notes
    fields = ['title']
    template_name = 'home.html'

def notes_add(request):
    if request.method == 'POST':
        form = NotesForm(request.POST)
        if form.is_valid():
            new_instance = form.save(commit = False)
            new_instance.user = request.user
            new_instance.save()
            form.save()
            return redirect('home')
    
    else:
        form = NotesForm()
    return render(request, 'notes_add.html', {'form':form})

def notes_detail(request, pk):
    note = get_object_or_404(Notes, pk=pk)
    return render(request, 'notes_detail.html', {'note':note})