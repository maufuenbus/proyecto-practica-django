from django.shortcuts import render
from .forms import *
from .models import Memorice, Metronomo


def index(request):
    return render(request, 'app/index.html')


def memorama(request):
    # return render(request, 'app/memorama.html')
    data = {
        'form': MemoriceForm,
    }
    if request.method == 'POST':
        formulario = MemoriceForm(data=request.POST)
        if formulario.is_valid():
            post = formulario.save(commit=False)
            post.acierto = request.POST["acierto"]
            post.tiempo = request.POST["tiempo"]
            post.movimientos = request.POST["movimientos"]
            # post.usuario_id = request.user.id
            formulario.save()
        else:
            formulario = MemoriceForm()
    return render(request, 'app/memorama.html', data)


def sonometro(request):
    return render(request, 'app/sonometro.html')


def metronomo(request):
    data = {
        'form': MetronomoForm,
    }
    if request.method == 'POST':
        formulario = MetronomoForm(data=request.POST)
        if formulario.is_valid():
            post = formulario.save(commit=False)
            post.bpm = request.POST["bpm"]
            post.beats = request.POST["beats"]
            post.duracion = request.POST["duracion"]
            # post.audio = request.POST['audio']
            # post.usuario_id = request.user.id
            formulario.save()
        else:
            formulario = MetronomoForm()
    return render(request, 'app/metronomo.html', data)

    # return render(request, 'app/metronomo.html')


def oscilograma(request):
    return render(request, 'app/oscilograma.html')


def medidor(request):
    return render(request, 'app/medidor-sonido.html')


def crucigrama(request):
    return render(request, 'app/crucigrama.html')
