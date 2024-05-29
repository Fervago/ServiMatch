from django.db import models
from django.contrib.auth.models import User

class Servicio(models.Model):
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField()
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, default=None)

    def __str__(self) -> str:
        return self.titulo


class OfrecerServicio(Servicio):
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    disponible_desde = models.DateField()
    disponible_hasta = models.DateField()
    fecha_publicacion = models.DateField(auto_now_add=True)


class ContratarServicio(Servicio):
    presupuesto_maximo = models.DecimalField(max_digits=10, decimal_places=2)
    fecha_solicitud = models.DateField(auto_now_add=True)
    fecha_limite = models.DateField()
