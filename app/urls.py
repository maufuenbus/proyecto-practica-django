from django.urls import path
from .views import index, memorama, metronomo, sonometro, oscilograma, medidor, crucigrama


urlpatterns = [
    path('', index, name="index"),
    path('memorama/', memorama, name="memorama"),
    path('metronomo/', metronomo, name="metronomo"),
    path('sonometro/', sonometro, name="sonometro"),
    path('oscilograma/', oscilograma, name="oscilograma"),
    path('medidor/', medidor, name="medidor"),
    path('crucigrama/', crucigrama, name="crucigrama"),
]
