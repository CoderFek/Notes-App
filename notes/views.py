from django.shortcuts import render, redirect, get_object_or_404
from .models import Notes
from .forms import NotesForm



from django.contrib.auth import login, authenticate, logout
from .forms import SignUpForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages



import bleach

# Create your views here.


def home_view(request):
    if request.user.is_authenticated:
        user_notes = Notes.objects.filter(user=request.user)
        return render(request, 'home.html', {'user_notes': user_notes})
    else:
        # Redirect to login page or display a message for non-authenticated users
        return redirect('login')


def notes_add(request):
    if request.user.is_authenticated:
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
            return render(request, 'notes_add.html', {'form': form})
    else:
        return redirect('login')


@login_required
def notes_detail(request, pk):
   
    note = get_object_or_404(Notes, pk=pk)
    allowed_tags = [
        'a', 'abbr', 'acronym', 'b', 'blockquote', 'code', 'em', 'i', 'li', 'ol', 'strong', 'ul',
        'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'p', 'br', 'span'
    ]
    sanitized_description = bleach.clean(note.description, tags=allowed_tags, strip=True)
    return render(request, 'notes_detail.html', {'note':note , 'sanitized_description':sanitized_description})


@login_required
def notes_edit(request, pk):
    note = get_object_or_404(Notes, pk=pk)
    if request.method == 'POST':
        form = NotesForm(request.POST, instance=note)
        if form.is_valid():
            form.save()
            messages.success(request, 'Changes Saved!')
            return redirect('home')
    else:
        form = NotesForm(instance=note)
    return render(request, 'notes_edit.html', {'form': form, 'note': note})


@login_required
def notes_delete(request, pk):
    note = get_object_or_404(Notes, pk=pk)
    if request.method == "POST":
        note.delete()
        return redirect('home')
    return render(request, 'notes_delete.html', {'note':note})


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'You are logged in!')
            return redirect('home')
        else:
            messages.error(request, 'Invalid username or password.')
    return render(request, 'login.html', {})


def logout_view(request):
    logout(request)
    return redirect('home')


def signup_view(request):
    form = SignUpForm()
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        
    return render(request, 'register.html', {'form':form})