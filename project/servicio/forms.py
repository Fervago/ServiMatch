from django import forms
from . import models


class OfrecerServicioForm(forms.ModelForm):
    class Meta:
        model = models.OfrecerServicio
        fields = "__all__"
        widgets = {
            'disponible_desde': forms.DateInput(attrs={'type': 'date'}),
            'disponible_hasta': forms.DateInput(attrs={'type': 'date'}),
        }


class ContratarServicioForm(forms.ModelForm):
    class Meta:
        model = models.ContratarServicio
        fields = "__all__"
        widgets = {
                'fecha_limite': forms.DateInput(attrs={'type': 'date'}),
            }
