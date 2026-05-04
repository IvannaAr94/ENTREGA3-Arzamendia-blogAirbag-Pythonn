from django.db import models

class Integrante(models.Model):
    nombre = models.CharField(max_length=100)
    instrumento = models.CharField(max_length=100)
    descripcion = models.TextField()

    def __str__(self):
        return f"{self.nombre} - {self.instrumento}"

class Album(models.Model):
    titulo = models.CharField(max_length=150)
    anio = models.IntegerField(verbose_name='Año')
    descripcion = models.TextField()

    def __str__(self):
        return f"{self.titulo} ({self.anio})"

class Post(models.Model):
    titulo = models.CharField(max_length=200)
    subtitulo = models.CharField(max_length=200, blank=True)
    contenido = models.TextField()
    autor = models.CharField(max_length=100)
    fecha = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.titulo
