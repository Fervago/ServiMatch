from django.contrib import admin

from .models import OfrecerServicio, ContratarServicio, Opinion

admin.site.register(ContratarServicio)
admin.site.register(OfrecerServicio)
admin.site.register(Opinion)
