from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import login, authenticate, logout as django_logout
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from tienda.forms import SignUpForm
from .models import *
from django.db.models import Q

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
    if request.method == 'POST' and 'search' in request.POST:
        criteria = request.POST['search']
        discos = Disco.objects.filter(Q(titulo__icontains=criteria) | Q(artista__nombre__icontains=criteria) | Q(artista__pais__nombre__icontains=criteria) )
    else:
        discos = Disco.objects.all()
    generos = Genero.objects.all()
    return render(request, 'tienda/index.html', {'discos': discos, 'generos': generos})

def genre(request, slug):
    nombre = slug
    generos = Genero.objects.all()
    discos = Disco.objects.filter(genero__nombre=nombre)
    return render(request, 'tienda/index.html', {'discos': discos, 'generos': generos})