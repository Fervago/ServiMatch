from django import forms
from . import models


class OfrecerServicioForm(forms.ModelForm):
    class Meta:
        model = models.OfrecerServicio
        fields = "__all__"
        widgets = {
            'descripcion': forms.Textarea(attrs={'style': 'width: 300px; height: 80px;'}),
            'disponible_desde': forms.DateInput(attrs={'type': 'date'}),
            'disponible_hasta': forms.DateInput(attrs={'type': 'date'}),
        }


class ContratarServicioForm(forms.ModelForm):
    class Meta:
        model = models.ContratarServicio
        fields = "__all__"
        widgets = {
            'descripcion': forms.Textarea(attrs={'style': 'width: 300px; height: 80px;'}),
            'fecha_limite': forms.DateInput(attrs={'type': 'date'}),
            }
