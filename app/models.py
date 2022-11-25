from django.db import models

# Create your models here.


class Memorice(models.Model):
    acierto = models.CharField(max_length=200)
    tiempo = models.CharField(max_length=100)
    movimientos = models.CharField(max_length=100)
    # usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.movimientos

    # def nombre_registro(self):
    #     return "{},". format(self.usuario)

    # def __str__(self):
    #     return self.nombre_registro()


class Metronomo(models.Model):
    bpm = models.CharField(max_length=100)
    beats = models.CharField(max_length=100)
    duracion = models.CharField(max_length=100)
    timestamp = models.DateTimeField(auto_now_add=True)
    #audio = models.FileField()

    def __str__(self):
        return self.bpm
