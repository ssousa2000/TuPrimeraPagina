from django.shortcuts import render
from django.shortcuts import render, redirect
from .forms import AutorForm, ArticuloForm, ComentarioForm
from .models import Articulo
from django.shortcuts import render

def crear_autor(request):
    if request.method == 'POST':
        form = AutorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('crear_autor')
    else:
        form = AutorForm()
    return render(request, 'blog/crear_autor.html', {'form': form})

def crear_articulo(request):
    if request.method == 'POST':
        form = ArticuloForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('crear_articulo')
    else:
        form = ArticuloForm()
    return render(request, 'blog/crear_articulo.html', {'form': form})

def crear_comentario(request):
    if request.method == 'POST':
        form = ComentarioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('crear_comentario')
    else:
        form = ComentarioForm()
    return render(request, 'blog/crear_comentario.html', {'form': form})

def buscar_articulo(request):
    resultados = []
    if 'q' in request.GET:
        query = request.GET['q']
        resultados = Articulo.objects.filter(titulo__icontains=query)
    return render(request, 'blog/buscar_articulo.html', {'resultados': resultados})

def about_view(request):
    return render(request, 'blog/about.html')

