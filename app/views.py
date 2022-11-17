from django.shortcuts import render

def index(request):
    return render(request,'app/index.html')

def memorama(request):
    return render(request,'app/memorama.html')

def sonometro(request):
    return render(request,'app/sonometro.html')

def metronomo(request):
    return render(request,'app/metronomo.html')

def oscilograma(request):
    return render(request,'app/oscilograma.html')

def medidor(request):
    return render(request,'app/medidor-sonido.html')