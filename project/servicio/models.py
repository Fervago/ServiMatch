from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator

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



class Opinion(models.Model):
    servicio = models.ForeignKey(OfrecerServicio, on_delete=models.SET_NULL, null=True, blank= True)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    comentario = models.TextField()
    calificacion = models.IntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(5)])
    fecha_publicacion = models.DateField(auto_now_add=True)