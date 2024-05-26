from typing import Any
from django.db import models


class Servicio(models.Model):
    nombre = models.CharField(max_length=200)
    descripcion = models.TextField()

    def __str__(self) -> str:
        return self.nombre


class ServicioOfrecido(Servicio, models.Model):
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)

    precio = models.DecimalField(max_digits=10, decimal_places=2)
    disponible_desde = models.DateField()
    disponible_hasta = models.DateField()
    fecha_publicacion = models.DateField(auto_now_add=True)


class ServicioContratado(Servicio, models.Model):
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)

    presupuesto_maximo = models.DecimalField(max_digits=10, decimal_places=2)
    fecha_solicitud = models.DateField(auto_now_add=True)
    fecha_limite = models.DateField()
