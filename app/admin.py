from django.contrib import admin
from .models import Memorice, Metronomo


# MEMORICE
class memoriceAdmin(admin.ModelAdmin):
    list_display = ["acierto", "tiempo", "movimientos", "timestamp"]


admin.site.register(Memorice, memoriceAdmin)


# METRONOMO
class metronomoAdmin(admin.ModelAdmin):
    list_display = ["bpm", "beats", "duracion", "timestamp"]  # , "audio"


admin.site.register(Metronomo, metronomoAdmin)
