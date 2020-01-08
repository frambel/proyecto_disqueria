from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import login, authenticate, logout as django_logout
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from tienda.forms import SignUpForm

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('tienda:inicio')
    else:
        form = SignUpForm()
    return render(request, 'tienda/signup.html', {'form': form})

def inicio(request):
    return render(request, 'tienda/index.html')