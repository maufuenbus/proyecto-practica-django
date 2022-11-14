from django.urls import path
from .views import index, login, memorama, metronomo, sonometro, oscilograma

urlpatterns = [
    path('', index, name="index"),
    path('login', login, name="login"),
    path('memorama', memorama, name="memorama"),
    path('metronomo', metronomo, name="metronomo"),
    path('sonometro', sonometro, name="sonometro"),
    path('oscilograma', oscilograma, name="oscilograma"),
]

