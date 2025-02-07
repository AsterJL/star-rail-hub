from django.db import models
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User

# Create your models here.

# ENCICLOPEDIA

class Afiliacion (models.Model):
    nombre = models.CharField(max_length=50, verbose_name='Nombre')
    descripcion = models.CharField(max_length=300, verbose_name='Descripción')
    imagen = models.ImageField(upload_to='photos')
    personajes = models.ManyToManyField('Personaje', related_name='afiliacion') # ManyToMany a Personaje

    class Meta:
        verbose_name = 'Afiliación'
        verbose_name_plural = 'Afiliaciones'

    def __str__(self):
        return f"Afiliación: {self.nombre}"

class Enemigo (models.Model):
    nombre = models.CharField(max_length=50, verbose_name='Nombre')
    descripcion = models.CharField(max_length=300, verbose_name='Descripción')
    imagen = models.ImageField()

    class Meta:
        verbose_name = 'Enemigo'
        verbose_name_plural = 'Enemigos'

    def __str__(self):
        return f"Enemigo: {self.nombre}"
    
class ImagenMapa (models.Model):
    nombre = models.CharField(max_length=50, verbose_name='Nombre')
    imagen = models.ImageField()
    mapas = models.ManyToManyField('Mapa', related_name='imagenesMapa') # ManyToMany a Mapa

    class Meta:
        verbose_name = 'Imagen de mapa'
        verbose_name_plural = 'Imágenes de mapa'

    def __str__(self):
        return f"Imagen de mapa: {self.nombre}"

class Mapa (models.Model):
    nombre = models.CharField(max_length=50, verbose_name='Nombre')
    # imagenesMapa = models.ManyToManyField(ImagenMapa)

    class Meta:
        verbose_name = 'Mapa'
        verbose_name_plural = 'Mapas'

    def __str__(self):
        return f"Mapa: {self.nombre}"
    
class ImagenModo (models.Model):
    nombre = models.CharField(max_length=50, verbose_name='Nombre')
    imagen = models.ImageField()
    modos = models.ManyToManyField('ModoJuego', related_name='imagenesModo') # ManyToMany a ModoJuego

    class Meta:
        verbose_name = 'Imagen de modo de juego'
        verbose_name_plural = 'Imágenes de modo de juego'

    def __str__(self):
        return f"Imagen de modo de juego: {self.nombre}"
    
class ModoJuego (models.Model):
    nombre = models.CharField(max_length=50, verbose_name='Nombre')
    descripcion = models.CharField(max_length=300, verbose_name='Descripción')
    # imagenes = models.ManyToManyField(ImagenModo)

    class Meta:
        verbose_name = 'Modo de juego'
        verbose_name_plural = 'Modos de juego'

    def __str__(self):
        return f"Modo de juego: {self.nombre}"
    
class Rareza (models.Model):
    nombre = models.CharField(max_length=50, verbose_name='Nombre')
    imagen = models.ImageField()

    class Meta:
        verbose_name = 'Rareza'
        verbose_name_plural = 'Rarezas'

    def __str__(self):
        return f"Rareza: {self.nombre}"
    
class Funcion (models.Model):
    nombre = models.CharField(max_length=50, verbose_name='Nombre')
    descripcion = models.CharField(max_length=300, verbose_name='Descripción')
    imagen = models.ImageField()

    class Meta:
        verbose_name = 'Funcion'
        verbose_name_plural = 'Funciones'

    def __str__(self):
        return f"Funcion: {self.nombre}"
    
# MATERIAL

class MetodoObtencion (models.Model):
    metodo = models.CharField(max_length=50, verbose_name='Método')

    class Meta:
        verbose_name = 'Método de obtención'
        verbose_name_plural = 'Métodos de obtención'

    def __str__(self):
        return f"Método de obtención: {self.metodo}"

class Material (models.Model):
    nombre = models.CharField(max_length=50, verbose_name='Nombre')
    rareza = models.ForeignKey(Rareza, on_delete=models.CASCADE, related_name='material')
    descripcion = models.CharField(max_length=300, verbose_name='Descripción')
    obtencion = models.ManyToManyField(MetodoObtencion) # FK a MetodoObtencion (varios MetodoObtencion)
    imagen = models.ImageField()

    class Meta:
        verbose_name = 'Material'
        verbose_name_plural = 'Materiales'

    def __str__(self):
        return f"Material: {self.nombre}"
    
# EQUIPO 

class PiezaEquipo (models.Model):
    nombre = models.CharField(max_length=50, verbose_name='Nombre')
    imagen = models.ImageField()

    class Meta:
        verbose_name = 'Pieza'
        verbose_name_plural = 'Piezas'

    def __str__(self):
        return f"Pieza: {self.nombre}"

class Equipo (models.Model):
    nombre = models.CharField(max_length=50, verbose_name='Nombre')
    rareza = models.ForeignKey(Rareza, on_delete=models.CASCADE, related_name='equipo')
    bono = models.CharField(max_length=300, verbose_name='Bono')
    piezas = models.ManyToManyField(PiezaEquipo) # FK a PiezaEquipo (varias PiezaEquipo)
    personajes = models.ManyToManyField('Personaje') # FK a Personaje (varios Personaje)

    class Meta:
        verbose_name = 'Equipo'
        verbose_name_plural = 'Equipos'

    def __str__(self):
        return f"Equipo: {self.nombre}"
    
# ARMA

class HabilidadArma (models.Model):
    nombre = models.CharField(max_length=50, verbose_name='Nombre')
    descripcion = models.CharField(max_length=300, verbose_name='Descripción')

    class Meta:
        verbose_name = 'Habilidad de Arma'
        verbose_name_plural = 'Habilidades de Arma'

    def __str__(self):
        return f"Habilidad de Arma: {self.nombre}"
    
class ImagenArma (models.Model):
    nombre = models.CharField(max_length=50, verbose_name='Nombre')
    imagen = models.ImageField()
    armas = models.ManyToManyField('Arma', related_name='imagenesArma') # ManyToMany a Arma

    class Meta:
        verbose_name = 'Imagen de modo de juego'
        verbose_name_plural = 'Imágenes de modo de juego'

    def __str__(self):
        return f"Imagen de modo de juego: {self.nombre}"

class Arma (models.Model):
    # Informacion general
    nombre = models.CharField(max_length=50, verbose_name='Nombre')
    rareza = models.ForeignKey(Rareza, on_delete=models.CASCADE, related_name='arma')
    funcion = models.ForeignKey(Funcion, on_delete=models.CASCADE, related_name='arma')
    imagenes = models.ManyToManyField(ImagenArma)
    # Atributos según el nivel
    habilidad = models.ManyToManyField(HabilidadArma) # FK a HabilidadArma (varias HabilidadArma)
    personajes = models.ManyToManyField('Personaje') # FK a Personaje (varios Personaje)

    class Meta:
        verbose_name = 'Arma'
        verbose_name_plural = 'Armas'

    def __str__(self):
        return f"Arma: {self.nombre}"
    
# PERSONAJE

class HabilidadPersonaje (models.Model):
    nombre = models.CharField(max_length=50, verbose_name='Nombre')
    tipo = models.CharField(max_length=50, verbose_name='Tipo') # Activa / Pasiva
    descripcion = models.CharField(max_length=300, verbose_name='Descripción')
    materiales = models.ManyToManyField(Material) # FK a Material (varios Material)
    imagen = models.ImageField()

    class Meta:
        verbose_name = 'Habilidad de Personaje'
        verbose_name_plural = 'Habilidades de Personaje'

    def __str__(self):
        return f"Habilidad de Personaje: {self.nombre}"
    
class ElementoPersonaje (models.Model):
    nombre = models.CharField(max_length=50, verbose_name='Nombre')
    imagen = models.ImageField()

    class Meta:
        verbose_name = 'Elemento'
        verbose_name_plural = 'Elementos'

    def __str__(self):
        return f"Elemento: {self.nombre}"
    
class ImagenPersonaje (models.Model):
    nombre = models.CharField(max_length=50, verbose_name='Nombre')
    imagen = models.ImageField()
    personajes = models.ManyToManyField('Personaje', related_name='imagenesPersonaje') # ManyToMany a Personaje

    class Meta:
        verbose_name = 'Imagen de modo de juego'
        verbose_name_plural = 'Imágenes de modo de juego'

    def __str__(self):
        return f"Imagen de modo de juego: {self.nombre}"

class Personaje (models.Model):
    # Informacion general
    nombre = models.CharField(max_length=50, verbose_name='Nombre')
    titulo = models.CharField(max_length=50, verbose_name='Título')
    afiliacion = models.ForeignKey(Afiliacion, on_delete=models.CASCADE, related_name='personaje')
    rareza = models.ForeignKey(Rareza, on_delete=models.CASCADE, related_name='personaje')
    funcion = models.ForeignKey(Funcion, on_delete=models.CASCADE, related_name='personaje')
    elemento = models.ForeignKey(ElementoPersonaje, on_delete=models.CASCADE, related_name='personaje')
    descripcion = models.CharField(max_length=300, verbose_name='Descripción')
    imagenes = models.ManyToManyField(ImagenPersonaje)
    # Atributos según el nivel
    habilidades = models.ManyToManyField(HabilidadPersonaje) # FK a HabilidadPersonaje (varias HabilidadPersonaje)
    armas = models.ManyToManyField(Arma) # FK a Arma (varias Arma)
    equipo = models.ManyToManyField(Equipo) # FK a Equipo (varios Equipo)
    personajes = models.ManyToManyField('Personaje') # FK a Personaje (varios Personaje)

    class Meta:
        verbose_name = 'Personaje'
        verbose_name_plural = 'Personajes'

    def __str__(self):
        return f"Personaje: {self.nombre}"
    
