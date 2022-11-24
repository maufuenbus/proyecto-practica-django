from django import forms
from .models import Memorice, Metronomo

# MEMORICE


class MemoriceForm(forms.ModelForm):
    acierto = forms.CharField(label='Cantidad de aciertos', widget=forms.TextInput(
        attrs={

            'placeholder': 'Ingresa cantidad de aciertos',
            'id': 'total_acierto'
        }))

    tiempo = forms.CharField(label='Cantidad de tiempo', widget=forms.TextInput(
        attrs={

            'placeholder': 'Ingresa cantidad de tiempo',
            'id': 'total_tiempo'
        }))

    movimientos = forms.CharField(label='Cantidad de movimientos', widget=forms.TextInput(
        attrs={

            'placeholder': 'Ingresa cantidad de movimientos',
            'id': 'total_movimientos'
        }))

    class Meta:
        model = Memorice
        fields = 'acierto', 'tiempo', 'movimientos',

######################### METRONOMO ###############################


class MetronomoForm(forms.ModelForm):
    bpm = forms.CharField(label='Cantidad de bpm', widget=forms.TextInput(
        attrs={

            'placeholder': 'Ingresa cantidad de bpm',
            'id': 'total_bpm'
        }))

    beats = forms.CharField(label='Cantidad de beats', widget=forms.TextInput(
        attrs={

            'placeholder': 'Ingresa cantidad de beats',
            'id': 'total_beats'
        }))

    duracion = forms.CharField(label='duracion', widget=forms.TextInput(
        attrs={

            'placeholder': 'Ingresa la duracion',
            'id': 'total_duracion'
        }))

    class Meta:
        model = Metronomo
        fields = 'bpm', 'beats', 'duracion',
