from django.urls import path

from .views import ContratarServicioList, OfrecerServicioList

app_name = "servicio"

urlpatterns = [
    path("servicio/contatar/", ContratarServicioList.as_view(),
         name="contratar_servicio"),
    path("servicio/ofrecer/", OfrecerServicioList.as_view(),
         name="ofrecer_servicio"),
]
