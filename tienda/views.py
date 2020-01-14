from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import login, authenticate, logout as django_logout
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from tienda.forms import SignUpForm
from .models import *
from django.db.models import Q
from django.core.mail import send_mail, BadHeaderError

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

def contacto(request):
    generos = Genero.objects.all()
    return render(request, 'tienda/contacto.html', {'generos': generos})

def enviar_mail(request):
    nombre = request.POST.get('nombre', '')
    body = request.POST.get('body', '')
    email = request.POST.get('email', '')
    generos = Genero.objects.all()
    if body and email and nombre:
        try:
            mensaje = 'De ' + nombre + '\n\n' + body
            send_mail('contacto', mensaje, email, ['info@amadeus.com'])
        except BadHeaderError:
            return render(request, 'tienda/contacto.html', {'generos': generos, 'message': 'Cabeceras invalidas.'})
        return render(request, 'tienda/contacto.html', {'generos': generos, 'message': 'Mensaje enviado con exito.'})
        # return redirect('/contacto/' , {'message': 'Mensaje enviado con exito.'})
    else:
        return render(request, 'tienda/contacto.html', {'generos': generos, 'message': 'Verifique que todos los campos han sido llenados y validos.'})