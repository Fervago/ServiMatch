from typing import Any
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    UpdateView,
)
from .models import OfrecerServicio, ContratarServicio
from .forms import OfrecerServicioForm, ContratarServicioForm



# ***** OFRECER Servicio

def index(request):
    return render(request, "servicio/index.html")

class OfrecerServicioList(ListView):
    model = OfrecerServicio
    template_name = "servicio/ofrecer_list.html"

    def get_queryset(self) -> QuerySet[Any]:
        queryset = super().get_queryset()
        busqueda = self.request.GET.get("busqueda")
        if busqueda:
            queryset = OfrecerServicio.objects.filter(
                Q(titulo__icontains=busqueda) 
            )
        return queryset

class OfrecerServicioDetail(DetailView):
    model = OfrecerServicio
    template_name = "servicio/ofrecer_detail.html"

class OfrecerServicioCreate(CreateView):
    model = OfrecerServicio
    form_class = OfrecerServicioForm
    template_name = "servicio/ofrecer.html"
    success_url = reverse_lazy('servicio:ofrecer_servicio_list')


class OfrecerServicioUpdate(UpdateView):
    model = OfrecerServicio
    form_class = OfrecerServicioForm
    template_name = "servicio/ofrecer.html"
    success_url = reverse_lazy('servicio:ofrecer_servicio_list')


class OfrecerServicioDelete(DeleteView):
    model = OfrecerServicio
    template_name = "servicio/ofrecer_delete.html"
    success_url = reverse_lazy('servicio:ofrecer_servicio_list')



# ***** CONTRATAR Servicio

class ContratarServicioList(ListView):
    model = ContratarServicio
    template_name = "servicio/contratar_list.html"

    def get_queryset(self) -> QuerySet[Any]:
        queryset = super().get_queryset()
        busqueda = self.request.GET.get("busqueda")
        if busqueda:
            queryset = ContratarServicio.objects.filter(
                Q(titulo__icontains=busqueda) 
            )
        return queryset

class ContratarServicioDetail(DetailView):
    model = ContratarServicio
    template_name = "servicio/contratar_detail.html"

class ContratarServicioCreate(CreateView):
    model = ContratarServicio
    form_class = ContratarServicioForm
    template_name = "servicio/contratar.html"
    success_url = reverse_lazy('servicio:contratar_servicio_list')


class ContratarServicioUpdate(UpdateView):
    model = ContratarServicio
    form_class = ContratarServicioForm
    template_name = "servicio/contratar.html"
    success_url = reverse_lazy('servicio:contratar_servicio_list')


class ContratarServicioDelete(DeleteView):
    model = ContratarServicio
    template_name = "servicio/contratar_delete.html"
    success_url = reverse_lazy('servicio:contratar_servicio_list')
