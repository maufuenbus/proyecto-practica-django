from django.contrib import admin
from .models import *
# Register your models here.

# VOCALIZACION


class VocalizacionAdmin(admin.ModelAdmin):
    list_display = ["usuario", "audio"]  # , "bpm", "beats", "timestamp"


admin.site.register(Vocalizacion, VocalizacionAdmin)


# MEMORICE


class MemoriceAdmin(admin.ModelAdmin):
    list_display = ["usuario", "acierto", "tiempo",
                    "movimientos", "timestamp"]


admin.site.register(Memorice, MemoriceAdmin)
