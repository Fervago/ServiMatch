from django.shortcuts import render

from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    UpdateView,
)

from .models import OfrecerServicio, ContratarServicio


class OfrecerServicioList(ListView):
    model = OfrecerServicio
    template_name = "servicio/ofrecer_list.html"

class ContratarServicioList(ListView):
    model = ContratarServicio
    template_name = "servicio/contratar_list.html"