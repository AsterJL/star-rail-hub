from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from django.views.generic import View, ListView, DetailView, UpdateView, DeleteView, CreateView
from django.urls import reverse_lazy
from django.db.models import Prefetch # Importamos esto para reducir el número de queries y mejorar así el rendimiento.
from django.contrib.auth.mixins import LoginRequiredMixin

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

    def get_context_data(self, **kwargs):
        contexto = super().get_context_data(**kwargs)
        personaje = self.object

        # Precarga las habilidades del personaje y sus materiales asociados en una sola consulta. Así con todos.
        personaje.habilidades.prefetch_related('materiales')
        personaje.armas.prefetch_related('imagenes_arma')
        personaje.equipo.all()
        personaje.sinergias.prefetch_related('imagenes_personaje')

        contexto['habilidades'] = personaje.habilidades.all()
        contexto['armas_recomendadas'] = personaje.armas.all()
        contexto['equipo_recomendado'] = personaje.equipo.all()
        contexto['sinergias'] = personaje.sinergias.all()

        return contexto

# class Personajes_Create (CreateView):
#     model = Personaje
#     template_name = 'app_proyecto/personajes_create.html'
#     context_object_name = 'personajes'
#     fields = '__all__'
#     success_url = reverse_lazy('personajes_list')

# class Personajes_Edit (UpdateView):
#     model = Personaje
#     template_name = 'app_proyecto/personajes_edit.html'
#     context_object_name = 'personajes'
#     fields = '__all__'
#     success_url = reverse_lazy('personajes_list')

# class Personajes_Delete (DeleteView):
#     model = Personaje
#     template_name = 'app_proyecto/personajes_delete.html'
#     context_object_name = 'personajes'

# ARMAS

class Armas_List (ListView):
    model = Arma
    template_name = 'app_proyecto/armas_list.html'
    context_object_name = 'armas'

    def get_context_data(self, **kwargs):
        contexto = super().get_context_data(**kwargs)

        contexto['rarezas'] = Rareza.objects.all()
        contexto['funciones'] = Funcion.objects.all()

        return contexto
    
    def get_queryset(self):
        query = super().get_queryset()
        
        rareza = self.request.GET.get('rareza')
        funcion = self.request.GET.get('funcion')
        nombre = self.request.GET.get('nombreArma')

        if rareza:
            query = query.filter(rareza__nombre=rareza)
        if funcion:
            query = query.filter(funcion__nombre=funcion)
        if nombre:
            query = query.filter(nombre__icontains=nombre)

        return query

class Armas_Details (DetailView):
    model = Arma
    template_name = 'app_proyecto/armas_details.html'
    context_object_name = 'armas'

    def get_context_data(self, **kwargs):
        contexto = super().get_context_data(**kwargs)
        arma = self.object

        # Precarga las habilidades de las armas y sus materiales asociados en una sola consulta. Así con todos.
        arma.personajes_armas.prefetch_related('imagenes_personaje')

        contexto['habilidades'] = arma.habilidad
        contexto['personajes_recomendados'] = arma.personajes_armas.all()

        return contexto

# class Armas_Create (CreateView):
#     model = Arma
#     template_name = 'app_proyecto/armas_create.html'
#     context_object_name = 'armas'
#     fields = '__all__'
#     success_url = reverse_lazy('armas_list')

# class Armas_Edit (UpdateView):
#     model = Arma
#     template_name = 'app_proyecto/armas_edit.html'
#     context_object_name = 'armas'
#     fields = '__all__'
#     success_url = reverse_lazy('armas_list')

# class Armas_Delete (DeleteView):
#     model = Arma
#     template_name = 'app_proyecto/armas_delete.html'
#     context_object_name = 'armas'

# EQUIPO

class Equipo_List (ListView):
    model = Equipo
    template_name = 'app_proyecto/equipo_list.html'
    context_object_name = 'equipos'

    def get_context_data(self, **kwargs):
        contexto = super().get_context_data(**kwargs)

        contexto['tipos_equipo'] = ['Principal', 'Secundario']

        return contexto
    
    def get_queryset(self):
        query = super().get_queryset()
        
        tipo = self.request.GET.get('tipoEquipo')
        nombre = self.request.GET.get('nombreEquipo')

        if tipo:
            query = query.filter(tipo__icontains=tipo)
        if nombre:
            query = query.filter(nombre__icontains=nombre)

        return query

class Equipo_Details (DetailView):
    model = Equipo
    template_name = 'app_proyecto/equipo_details.html'
    context_object_name = 'equipos'

# MATERIALES

class Materiales_List (ListView):
    model = Material
    template_name = 'app_proyecto/materiales_list.html'
    context_object_name = 'materiales'

    def get_context_data(self, **kwargs):
        contexto = super().get_context_data(**kwargs)

        contexto['rarezas'] = Rareza.objects.all()

        return contexto
    
    def get_queryset(self):
        query = super().get_queryset()
        
        rareza = self.request.GET.get('rareza')
        nombre = self.request.GET.get('nombreMaterial')

        if rareza:
            query = query.filter(rareza__nombre=rareza)
        if nombre:
            query = query.filter(nombre__icontains=nombre)

        return query

class Materiales_Details (DetailView):
    model = Material
    template_name = 'app_proyecto/materiales_details.html'
    context_object_name = 'materiales'

# ENCICLOPEDIA

def enciclopedia (request):
    return render(request, 'app_proyecto/enciclopedia.html')

# AFILIACIONES

# class Afiliaciones_List (ListView):
#     model = Afiliacion
#     template_name = 'app_proyecto/afiliaciones_list.html'
#     context_object_name = 'afiliaciones'

# class Afiliaciones_Details (DetailView):
#     model = Afiliacion
#     template_name = 'app_proyecto/afiliaciones_details.html'
#     context_object_name = 'afiliaciones'

# ENEMIGOS

# class Enemigos_List (ListView):
#     model = Enemigo
#     template_name = 'app_proyecto/enemigos_list.html'
#     context_object_name = 'enemigos'

# class Enemigos_Details (DetailView):
#     model = Enemigo
#     template_name = 'app_proyecto/enemigos_details.html'
#     context_object_name = 'enemigos'

# MAPAS

# class Mapas_List (ListView):
#     model = Mapa
#     template_name = 'app_proyecto/mapas_list.html'
#     context_object_name = 'mapas'

# class Mapas_Details (DetailView):
#     model = Mapa
#     template_name = 'app_proyecto/mapas_details.html'
#     context_object_name = 'mapas'

# RAREZAS

# class Rarezas_List (ListView):
#     model = Rareza
#     template_name = 'app_proyecto/rarezas_list.html'
#     context_object_name = 'rarezas'

# class Rarezas_Details (DetailView):
#     model = Rareza
#     template_name = 'app_proyecto/rarezas_details.html'
#     context_object_name = 'rarezas'

# FUNCIONES

# class Funciones_List (ListView):
#     model = Funcion
#     template_name = 'app_proyecto/funciones_list.html'
#     context_object_name = 'funciones'

# class Funciones_Details (DetailView):
#     model = Funcion
#     template_name = 'app_proyecto/funciones_details.html'
#     context_object_name = 'funciones'

# INVENTARIO



# FAVORITOS

class Favoritos_List(LoginRequiredMixin, ListView):
    model = Favorito
    template_name = 'app_proyecto/favoritos_list.html'
    context_object_name = 'favoritos'

    def get_queryset(self):
        return Favorito.objects.filter(usuario=self.request.user).select_related('personaje').prefetch_related('personaje__imagenes_personaje')
    
class Favoritos_Add(LoginRequiredMixin, ListView):
    model = Personaje
    template_name = 'app_proyecto/favoritos_add.html'
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

    def post(self, request, *args, **kwargs):
        ids = request.POST.getlist('personajes_ids')
        for personaje_id in ids:
            Favorito.objects.get_or_create(
                usuario=request.user,
                personaje_id=personaje_id
            )
        return redirect('favoritos_list')

# OTROS USUARIOS