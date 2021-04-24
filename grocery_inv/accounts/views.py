from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm

def register(request):
    """Register a new user."""
    form = UserCreationForm(request.POST or None)
    if form.is_valid():
        user = form.save()
        login(request, user)
        form = UserCreationForm()
        return redirect('inventory:index')
    
    context = {'form': form}
    return render(request, 'registration/register.html', context)
