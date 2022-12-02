from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models
# Create your models here.


class Vocalizacion(models.Model):
    usuario = models.ForeignKey(User,  on_delete=models.CASCADE)
    audio = models.FileField(upload_to='archivos_media')
    #bpm = models.CharField(max_length=100, null=True)
    #beats = models.CharField(max_length=100, null=True)
    #timestamp = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return str(self.usuario)


class Memorice(models.Model):
    acierto = models.CharField(max_length=200)
    tiempo = models.CharField(max_length=100)
    movimientos = models.CharField(max_length=100)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.usuario)


class VocalPalabras(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    audio = models.FileField(upload_to='archivos_media')

    def __str__(self):
        return str(self.usuario)


class VocalTexto(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    audio = models.FileField(upload_to='archivos_media')

    def __str__(self):
        return str(self.usuario)
