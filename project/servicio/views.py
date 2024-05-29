from typing import Any
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.db.models.query import QuerySet
from django.shortcuts import render, redirect
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

class OfrecerServicioList(LoginRequiredMixin, ListView):
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

class OfrecerServicioDetail(LoginRequiredMixin, DetailView):
    model = OfrecerServicio
    template_name = "servicio/ofrecer_detail.html"

class OfrecerServicioCreate(LoginRequiredMixin, CreateView):
    model = OfrecerServicio
    form_class = OfrecerServicioForm
    template_name = "servicio/ofrecer.html"
    success_url = reverse_lazy('servicio:ofrecer_servicio_list')


class OfrecerServicioUpdate(LoginRequiredMixin, UpdateView):
    model = OfrecerServicio
    form_class = OfrecerServicioForm
    template_name = "servicio/ofrecer.html"
    success_url = reverse_lazy('servicio:ofrecer_servicio_list')

    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if not obj.usuario == request.user: # type: ignore
            messages.error(request, "No tienes permiso para editar este servicio.")
            return redirect('servicio:ofrecer_servicio_detail', pk=obj.pk)
        return super().dispatch(request, *args, **kwargs)


class OfrecerServicioDelete(LoginRequiredMixin, DeleteView):
    model = OfrecerServicio
    template_name = "servicio/ofrecer_delete.html"
    success_url = reverse_lazy('servicio:ofrecer_servicio_list')

    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if not obj.usuario == request.user: # type: ignore 
            messages.error(request, "No tienes permiso para editar este servicio.")
            return redirect('servicio:ofrecer_servicio_detail', pk=obj.pk)
        return super().dispatch(request, *args, **kwargs)


# ***** CONTRATAR Servicio

class ContratarServicioList(LoginRequiredMixin, ListView):
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

class ContratarServicioDetail(LoginRequiredMixin, DetailView):
    model = ContratarServicio
    template_name = "servicio/contratar_detail.html"

class ContratarServicioCreate(LoginRequiredMixin, CreateView):
    model = ContratarServicio
    form_class = ContratarServicioForm
    template_name = "servicio/contratar.html"
    success_url = reverse_lazy('servicio:contratar_servicio_list')


class ContratarServicioUpdate(LoginRequiredMixin, UpdateView):
    model = ContratarServicio
    form_class = ContratarServicioForm
    template_name = "servicio/contratar.html"
    success_url = reverse_lazy('servicio:contratar_servicio_list')

    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if not obj.usuario == request.user: # type: ignore
            messages.error(request, "No tienes permiso para editar este servicio.")
            return redirect('servicio:contratar_servicio_detail', pk=obj.pk)
        return super().dispatch(request, *args, **kwargs)

class ContratarServicioDelete(LoginRequiredMixin, DeleteView):
    model = ContratarServicio
    template_name = "servicio/contratar_delete.html"
    success_url = reverse_lazy('servicio:contratar_servicio_list')

    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if not obj.usuario == request.user: # type: ignore
            messages.error(request, "No tienes permiso para editar este servicio.")
            return redirect('servicio:contratar_servicio_detail', pk=obj.pk)
        return super().dispatch(request, *args, **kwargs)