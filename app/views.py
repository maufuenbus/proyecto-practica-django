from django.shortcuts import render
from .forms import *
from .models import *
import os
from mysite.settings import MEDIA_ROOT
from django.http import HttpResponse
from audio.audio import Audio
from django.views.generic import View
from django.http import JsonResponse
from django.shortcuts import redirect


def index(request):
    return render(request, 'app/index.html')


def oscilograma(request):
    return render(request, 'app/oscilograma.html')


def medidor(request):
    return render(request, 'app/medidor-sonido.html')


def intensidad(request):
    return render(request, 'app/intensidad.html')


def eva_param_func(request):
    return render(request, 'app/eva_param_func.html')


def eva_param_text(request):
    return render(request, 'app/eva_param_text.html')


def crucigrama(request):
    return render(request, 'app/crucigrama.html')

###################### MEMORICE #######################
################ NO TOCAR DE MOMENTO ##################


def memorama(request):
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
            post.usuario_id = request.user.id
            formulario.save()
        else:
            formulario = MemoriceForm()
    return render(request, 'app/memorama.html', data)
    # return render(request, 'app/memorama.html')


########################## VOCALIZACION ################################
############## CONFIGURAR CORRECTAMENTE PARA GUARDAR#####################
class VocalizacionView(View):

    def get(self, request, *args, **kwargs):
        print(request.user.id)
        return render(request, 'app/vocalizacion.html')

    def post(self, request, *args, **kwargs):
        print("hola estoy en el post")
        audio = Audio()
        audio.grabarAudio(str(request.user.id))
        return render(request, 'app/vocalizacion.html')
