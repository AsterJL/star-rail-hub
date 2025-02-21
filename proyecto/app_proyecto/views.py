from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from django.views.generic import View, ListView, DetailView, UpdateView, DeleteView, CreateView
from django.urls import reverse_lazy

# Create your views here.

def principal (request):
    return render(request, 'app_proyecto/principal.html')

# PERSONAJES

class Personajes_List (ListView):
    model = Personaje
    template_name = 'app_proyecto/personajes_list.html'
    context_object_name = 'personajes'

    def get_context_data(self, **kwargs):
        contexto = super().get_context_data(**kwargs)
    
        contexto['elementos'] = ElementoPersonaje.objects.all()
        contexto['rarezas'] = Rareza.objects.all()
        contexto['funciones'] = Funcion.objects.all()

        return contexto
    
    def get_queryset(self):
        query = super().get_queryset()
        
        elemento = self.request.GET.get('elemento')
        rareza = self.request.GET.get('rareza')
        funcion = self.request.GET.get('funcion')
        nombre = self.request.GET.get('nombrePersonaje')

        if elemento:
            query = query.filter(elemento__nombre=elemento)
        if rareza:
            query = query.filter(rareza__nombre=rareza)
        if funcion:
            query = query.filter(funcion__nombre=funcion)
        if nombre:
            query = query.filter(nombre__icontains=nombre)

        return query

class Personajes_Details (DetailView):
    model = Personaje
    template_name = 'app_proyecto/personajes_details.html'
    context_object_name = 'personajes'

class Personajes_Create (CreateView):
    model = Personaje
    template_name = 'app_proyecto/personajes_create.html'
    context_object_name = 'personajes'
    fields = '__all__'
    success_url = reverse_lazy('personajes_list')

class Personajes_Edit (UpdateView):
    model = Personaje
    template_name = 'app_proyecto/personajes_edit.html'
    context_object_name = 'personajes'
    fields = '__all__'
    success_url = reverse_lazy('personajes_list')

class Personajes_Delete (DeleteView):
    model = Personaje
    template_name = 'app_proyecto/personajes_delete.html'
    context_object_name = 'personajes'

# ARMAS

class Armas_List (ListView):
    model = Arma
    template_name = 'app_proyecto/armas_list.html'
    context_object_name = 'armas'

class Armas_Details (DetailView):
    model = Arma
    template_name = 'app_proyecto/armas_details.html'
    context_object_name = 'armas'

class Armas_Create (CreateView):
    model = Arma
    template_name = 'app_proyecto/armas_create.html'
    context_object_name = 'armas'
    fields = '__all__'
    success_url = reverse_lazy('armas_list')

class Armas_Edit (UpdateView):
    model = Arma
    template_name = 'app_proyecto/armas_edit.html'
    context_object_name = 'armas'
    fields = '__all__'
    success_url = reverse_lazy('armas_list')

class Armas_Delete (DeleteView):
    model = Arma
    template_name = 'app_proyecto/armas_delete.html'
    context_object_name = 'armas'

# EQUIPO

class Equipo_List (ListView):
    model = Equipo
    template_name = 'app_proyecto/equipo_list.html'
    context_object_name = 'equipos'

class Equipo_Details (DetailView):
    model = Equipo
    template_name = 'app_proyecto/equipo_details.html'
    context_object_name = 'equipos'

# MATERIALES

class Materiales_List (ListView):
    model = Material
    template_name = 'app_proyecto/materiales_list.html'
    context_object_name = 'materiales'

class Materiales_Details (DetailView):
    model = Material
    template_name = 'app_proyecto/materiales_details.html'
    context_object_name = 'materiales'

# ENCICLOPEDIA

def enciclopedia (request):
    return render(request, 'app_proyecto/enciclopedia.html')

# AFILIACIONES

class Afiliaciones_List (ListView):
    model = Afiliacion
    template_name = 'app_proyecto/afiliaciones_list.html'
    context_object_name = 'afiliaciones'

class Afiliaciones_Details (DetailView):
    model = Afiliacion
    template_name = 'app_proyecto/afiliaciones_details.html'
    context_object_name = 'afiliaciones'

# ENEMIGOS

class Enemigos_List (ListView):
    model = Enemigo
    template_name = 'app_proyecto/enemigos_list.html'
    context_object_name = 'enemigos'

class Enemigos_Details (DetailView):
    model = Enemigo
    template_name = 'app_proyecto/enemigos_details.html'
    context_object_name = 'enemigos'

# MAPAS

class Mapas_List (ListView):
    model = Mapa
    template_name = 'app_proyecto/mapas_list.html'
    context_object_name = 'mapas'

class Mapas_Details (DetailView):
    model = Mapa
    template_name = 'app_proyecto/mapas_details.html'
    context_object_name = 'mapas'

# RAREZAS

class Rarezas_List (ListView):
    model = Rareza
    template_name = 'app_proyecto/rarezas_list.html'
    context_object_name = 'rarezas'

class Rarezas_Details (DetailView):
    model = Rareza
    template_name = 'app_proyecto/rarezas_details.html'
    context_object_name = 'rarezas'

# FUNCIONES

class Funciones_List (ListView):
    model = Funcion
    template_name = 'app_proyecto/funciones_list.html'
    context_object_name = 'funciones'

class Funciones_Details (DetailView):
    model = Funcion
    template_name = 'app_proyecto/funciones_details.html'
    context_object_name = 'funciones'