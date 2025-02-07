from django.contrib import admin

# Register your models here.

from .models import *

admin.site.register(Afiliacion)
admin.site.register(Enemigo)
admin.site.register(Mapa)
admin.site.register(ImagenMapa)
admin.site.register(Rareza)
admin.site.register(Funcion)

admin.site.register(MetodoObtencion)
admin.site.register(Material)

admin.site.register(Equipo)
admin.site.register(PiezaEquipo)

admin.site.register(HabilidadArma)
admin.site.register(Arma)
admin.site.register(ImagenArma)

admin.site.register(HabilidadPersonaje)
admin.site.register(ElementoPersonaje)
admin.site.register(Personaje)
admin.site.register(ImagenPersonaje)