from django.contrib import admin
from django.urls import path, include
from . import views
from .views import *

urlpatterns=[
    path('', views.principal, name='principal'),

    path('personajes/', Personajes_List.as_view(), name='personajes_list'),
    path('personajes/<int:pk>/', Personajes_Details.as_view(), name='personajes_details'),
    # path('personajes/create/', Personajes_Create.as_view(), name='personajes_create'),
    # path('personajes/<int:pk>/edit/', Personajes_Edit.as_view(), name='personajes_edit'),
    # path('personajes/<int:pk>/delete/', Personajes_Delete.as_view(), name='personajes_delete'),

    path('armas/', Armas_List.as_view(), name='armas_list'),
    path('armas/<int:pk>/', Armas_Details.as_view(), name='armas_details'),
    # path('armas/create/', Armas_Create.as_view(), name='armas_create'),
    # path('armas/<int:pk>/edit/', Armas_Edit.as_view(), name='armas_edit'),
    # path('armas/<int:pk>/delete/', Armas_Delete.as_view(), name='armas_delete'),

    path('equipo/', Equipo_List.as_view(), name='equipo_list'),
    path('equipo/<int:pk>/', Equipo_Details.as_view(), name='equipo_details'),

    path('materiales/', Materiales_List.as_view(), name='materiales_list'),
    path('materiales/<int:pk>', Materiales_Details.as_view(), name='materiales_details'),

    path('enciclopedia/', views.enciclopedia, name='enciclopedia'),

    path('enciclopedia/afiliaciones/', Afiliaciones_List.as_view(), name='afiliaciones_list'),
    # path('enciclopedia/afiliaciones/<int:pk>/', Afiliaciones_Details.as_view(), name='afiliaciones_details'),
    
    # path('enciclopedia/enemigos/', Enemigos_List.as_view(), name='enemigos_list'),
    # path('enciclopedia/enemigos/<int:pk>/', Enemigos_Details.as_view(), name='enemigos_details'),
    
    # path('enciclopedia/mapas/', Mapas_List.as_view(), name='mapas_list'),
    # path('enciclopedia/mapas/<int:pk>/', Mapas_Details.as_view(), name='mapas_details'),
    
    # path('enciclopedia/rarezas/', Rarezas_List.as_view(), name='rarezas_list'),
    # path('enciclopedia/rarezas/<int:pk>/', Rarezas_Details.as_view(), name='rarezas_details'),
    
    path('enciclopedia/funciones/', Funciones_List.as_view(), name='funciones_list'),
    # path('enciclopedia/funciones/<int:pk>/', Funciones_Details.as_view(), name='funciones_details'),

    path('favoritos/', Favoritos_List.as_view(), name='favoritos_list'),
    path('favoritos/add/', Favoritos_Add.as_view(), name='favoritos_add'),
    path('favoritos/delete/<int:pk>/', Favoritos_Delete.as_view(), name='favoritos_delete'),

    path('registro/', RegistroView.as_view(), name='registro'),

    path('inventario/', InventarioListView.as_view(), name='inventario_list'),
    path('inventario/add/', InventarioCreateView.as_view(), name='inventario_add'),
    path('inventario/delete/<int:pk>/', InventarioDeleteView.as_view(), name='inventario_delete'),
    path('inventario/update/<int:pk>/', InventarioUpdateView.as_view(), name='inventario_update'),
]