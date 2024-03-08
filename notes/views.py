from django.shortcuts import render, redirect, get_object_or_404, reverse
from .models import Notes
from django.views.generic import ListView
from .forms import NotesForm
import bleach

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
    allowed_tags = [
        'a', 'abbr', 'acronym', 'b', 'blockquote', 'code', 'em', 'i', 'li', 'ol', 'strong', 'ul',
        'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'p', 'br', 'span'
    ]
    sanitized_description = bleach.clean(note.description, tags=allowed_tags, strip=True)
    return render(request, 'notes_detail.html', {'note':note , 'sanitized_description':sanitized_description})


def notes_edit(request, pk):
    note = get_object_or_404(Notes, pk=pk)
    if request.method == 'POST':
        form = NotesForm(request.POST, instance=note)
        if form.is_valid():
            form.save()
            return redirect('notes_detail', pk=pk)
    else:
        form = NotesForm(instance=note)
    return render(request, 'notes_edit.html', {'form': form, 'note': note})


def notes_delete(request, pk):
    note = get_object_or_404(Notes, pk=pk)
    if request.method == "POST":
        note.delete()
        return redirect('home')
    return render(request, 'notes_delete.html', {'note':note})