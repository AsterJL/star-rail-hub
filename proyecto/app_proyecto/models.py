from django.db import models
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User

# Create your models here.

# ENCICLOPEDIA

class Afiliacion(models.Model):
    nombre = models.CharField(max_length=50, verbose_name='Nombre')
    descripcion = models.CharField(max_length=2000, verbose_name='Descripción')
    imagen = models.ImageField(upload_to='images/photos')

    class Meta:
        verbose_name = 'Afiliación'
        verbose_name_plural = 'Afiliaciones'

    def __str__(self):
        return f"Afiliación: {self.nombre}"


class Enemigo(models.Model):
    nombre = models.CharField(max_length=100, verbose_name='Nombre')
    descripcion = models.CharField(max_length=2000, verbose_name='Descripción')
    imagen = models.ImageField(upload_to='images/enemies')

    class Meta:
        verbose_name = 'Enemigo'
        verbose_name_plural = 'Enemigos'

    def __str__(self):
        return f"Enemigo: {self.nombre}"


class Mapa(models.Model):
    nombre = models.CharField(max_length=50, verbose_name='Nombre')

    class Meta:
        verbose_name = 'Mapa'
        verbose_name_plural = 'Mapas'

    def __str__(self):
        return f"Mapa: {self.nombre}"


class ImagenMapa(models.Model):
    nombre = models.CharField(max_length=100, verbose_name='Nombre')
    imagen = models.ImageField(upload_to='images/maps')
    mapa = models.ForeignKey(Mapa, on_delete=models.CASCADE, related_name='imagenes_mapa')

    class Meta:
        verbose_name = 'Imagen de mapa'
        verbose_name_plural = 'Imágenes de mapa'

    def __str__(self):
        return f"Imagen de mapa: {self.nombre}"
    

class Rareza(models.Model):
    nombre = models.CharField(max_length=100, verbose_name='Nombre')
    imagen = models.ImageField(upload_to='images/rarities')

    class Meta:
        verbose_name = 'Rareza'
        verbose_name_plural = 'Rarezas'

    def __str__(self):
        return f"Rareza: {self.nombre}"


class Funcion(models.Model):
    nombre = models.CharField(max_length=100, verbose_name='Nombre')
    descripcion = models.CharField(max_length=2000, verbose_name='Descripción')
    imagen = models.ImageField(upload_to='images/functions')

    class Meta:
        verbose_name = 'Función'
        verbose_name_plural = 'Funciones'

    def __str__(self):
        return f"Función: {self.nombre}"


# MATERIAL

class MetodoObtencion(models.Model):
    metodo = models.CharField(max_length=300, verbose_name='Método')

    class Meta:
        verbose_name = 'Método de obtención'
        verbose_name_plural = 'Métodos de obtención'

    def __str__(self):
        return f"Método de obtención: {self.metodo}"


class Material(models.Model):
    nombre = models.CharField(max_length=100, verbose_name='Nombre')
    rareza = models.ForeignKey(Rareza, on_delete=models.CASCADE, related_name='materiales_rareza')
    descripcion = models.CharField(max_length=2000, verbose_name='Descripción')
    obtencion = models.ManyToManyField(MetodoObtencion, related_name='materiales_obtencion')
    imagen = models.ImageField(upload_to='images/materials')

    class Meta:
        verbose_name = 'Material'
        verbose_name_plural = 'Materiales'

    def __str__(self):
        return f"Material: {self.nombre}"


# EQUIPO

class Equipo(models.Model):
    TIPOS_EQUIPO = [
        ('Principal', 'Principal'),
        ('Secundario', 'Secundario'),
    ]

    nombre = models.CharField(max_length=100, verbose_name='Nombre')
    rareza = models.ForeignKey(Rareza, on_delete=models.CASCADE, related_name='equipos_rareza')
    bono = models.CharField(max_length=2000, verbose_name='Bono')
    tipo = models.CharField(max_length=100, choices=TIPOS_EQUIPO, verbose_name='Tipo', default='Principal')  # Principal / Secundario
    imagen = models.ImageField(upload_to='images/equipment')

    class Meta:
        verbose_name = 'Equipo'
        verbose_name_plural = 'Equipos'

    def __str__(self):
        return f"Equipo: {self.nombre}"

class PiezaEquipo(models.Model):
    TIPOS_PIEZA = [
        ('Casco', 'Casco'),
        ('Manos', 'Manos'),
        ('Pecho', 'Pecho'),
        ('Botas', 'Botas'),
        ('Orbe', 'Orbe'),
        ('Cuerda', 'Cuerda'),
    ]

    nombre = models.CharField(max_length=100, verbose_name='Nombre')
    imagen = models.ImageField(upload_to='images/equipment_pieces')
    tipo = models.CharField(max_length=100, choices=TIPOS_PIEZA, verbose_name='Tipo', default='Casco')  # Casco / Manos / Pecho / Botas / Orbe / Cuerda
    equipo = models.ForeignKey(Equipo, on_delete=models.CASCADE, related_name='piezas_equipo')

    class Meta:
        verbose_name = 'Pieza de equipo'
        verbose_name_plural = 'Piezas de equipo'

    def __str__(self):
        return f"Pieza de equipo: {self.nombre}"

# ARMA

class HabilidadArma(models.Model):
    nombre = models.CharField(max_length=100, verbose_name='Nombre')
    descripcion = models.CharField(max_length=2000, verbose_name='Descripción')

    class Meta:
        verbose_name = 'Habilidad de arma'
        verbose_name_plural = 'Habilidades de arma'

    def __str__(self):
        return f"Habilidad de arma: {self.nombre}"


class Arma(models.Model):
    nombre = models.CharField(max_length=100, verbose_name='Nombre')
    rareza = models.ForeignKey(Rareza, on_delete=models.CASCADE, related_name='armas_rareza')
    funcion = models.ForeignKey(Funcion, on_delete=models.CASCADE, related_name='armas_funcion')
    habilidad = models.OneToOneField(HabilidadArma, on_delete=models.CASCADE, related_name='arma_habilidad')

    class Meta:
        verbose_name = 'Arma'
        verbose_name_plural = 'Armas'

    def __str__(self):
        return f"Arma: {self.nombre}"

class ImagenArma(models.Model):
    nombre = models.CharField(max_length=100, verbose_name='Nombre')
    imagen = models.ImageField(upload_to='images/weapons')
    arma = models.ForeignKey(Arma, on_delete=models.CASCADE, related_name='imagenes_arma')

    class Meta:
        verbose_name = 'Imagen del Arma'
        verbose_name_plural = 'Imágenes del Arma'

    def __str__(self):
        return f"Imagen del Arma: {self.nombre}"

# PERSONAJE

class HabilidadPersonaje(models.Model):
    TIPOS_HABILIDAD = [
        ('ATQ básico', 'ATQ básico'),
        ('Habilidad básica', 'Habilidad básica'),
        ('Habilidad definitiva', 'Habilidad definitiva'),
        ('Talento', 'Talento'),
    ]

    nombre = models.CharField(max_length=100, verbose_name='Nombre')
    tipo = models.CharField(max_length=100, choices=TIPOS_HABILIDAD, verbose_name='Tipo', default='ATQ básico')  # ATQ básico / Habilidad básica / Habilidad definitiva / Talento
    descripcion = models.CharField(max_length=2000, verbose_name='Descripción')
    materiales = models.ManyToManyField(Material, related_name='habilidades_materiales')
    imagen = models.ImageField(upload_to='images/skills')

    class Meta:
        verbose_name = 'Habilidad de personaje'
        verbose_name_plural = 'Habilidades de personaje'

    def __str__(self):
        return f"Habilidad de personaje: {self.nombre}"


class ElementoPersonaje(models.Model):
    nombre = models.CharField(max_length=100, verbose_name='Nombre')
    imagen = models.ImageField(upload_to='images/elements')

    class Meta:
        verbose_name = 'Elemento'
        verbose_name_plural = 'Elementos'

    def __str__(self):
        return f"Elemento: {self.nombre}"


class Personaje(models.Model):
    nombre = models.CharField(max_length=100, verbose_name='Nombre')
    titulo = models.CharField(max_length=100, blank=True, verbose_name='Título')
    afiliacion = models.ForeignKey(Afiliacion, blank=True, on_delete=models.SET_NULL, null=True, related_name='personajes_afiliacion')
    rareza = models.ForeignKey(Rareza, on_delete=models.SET_NULL, null=True, related_name='personajes_rareza')
    funcion = models.ForeignKey(Funcion, on_delete=models.SET_NULL, null=True, related_name='personajes_funcion')
    elemento = models.ForeignKey(ElementoPersonaje, on_delete=models.SET_NULL, null=True, related_name='personajes_elemento')
    descripcion = models.CharField(max_length=2000, blank=True, verbose_name='Descripción')
    habilidades = models.ManyToManyField(HabilidadPersonaje, related_name='personajes_habilidades')
    armas = models.ManyToManyField(Arma, blank=True, related_name='personajes_armas')
    equipo = models.ManyToManyField(Equipo, blank=True, related_name='personajes_equipo')
    sinergias = models.ManyToManyField('self', blank=True, related_name='personajes_sinergias')

    class Meta:
        verbose_name = 'Personaje'
        verbose_name_plural = 'Personajes'

    def __str__(self):
        return f"Personaje: {self.nombre}"
    
class ImagenPersonaje(models.Model):
    nombre = models.CharField(max_length=100, verbose_name='Nombre')
    imagen = models.ImageField(upload_to='images/characters')
    personaje = models.ForeignKey(Personaje, on_delete=models.CASCADE, related_name='imagenes_personaje')

    class Meta:
        verbose_name = 'Imagen del Personaje'
        verbose_name_plural = 'Imágenes del Personaje'

    def __str__(self):
        return f"Imagen del Personaje: {self.nombre}"
