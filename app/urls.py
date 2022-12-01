from django.urls import path
from .views import index, memorama, VocalizacionView, intensidad, oscilograma, medidor


urlpatterns = [
    path('', index, name="index"),
    path('memorama/', memorama, name="memorama"),
    path('vocalizacion/', VocalizacionView.as_view(), name="vocalizacion"),
    path('intensidad/', intensidad, name="intensidad"),
    path('oscilograma/', oscilograma, name="oscilograma"),
    path('medidor/', medidor, name="medidor"),
]
