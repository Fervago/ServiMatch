from django.urls import path

from .views import (OfrecerServicioList,
                    OfrecerServicioDetail,
                    OfrecerServicioCreate,
                    OfrecerServicioUpdate,
                    OfrecerServicioDelete,
                    ContratarServicioList,
                    ContratarServicioDetail,
                    ContratarServicioCreate,
                    ContratarServicioUpdate,
                    ContratarServicioDelete,
                    OpinionServicioList,
                    OpinionServicioCreate,
                    index
                    )

app_name = "servicio"

urlpatterns = [
    path("", index ,name="index"),
    path("ofrecer/list/", OfrecerServicioList.as_view(),name="ofrecer_servicio_list"),
    path("ofrecer/detail/<int:pk>/", OfrecerServicioDetail.as_view(),name="ofrecer_servicio_detail"),
    path("ofrecer/create/", OfrecerServicioCreate.as_view(),name="ofrecer_servicio_create"),
    path("ofrecer/update/<int:pk>/", OfrecerServicioUpdate.as_view(),name="ofrecer_servicio_update"),
    path("ofrecer/delete/<int:pk>/", OfrecerServicioDelete.as_view(),name="ofrecer_servicio_delete"),
    path("contratar/list/", ContratarServicioList.as_view(),name="contratar_servicio_list"),
    path("contratar/detail/<int:pk>/", ContratarServicioDetail.as_view(),name="contratar_servicio_detail"),
    path("contratar/create/", ContratarServicioCreate.as_view(),name="contratar_servicio_create"),
    path("contratar/update/<int:pk>/", ContratarServicioUpdate.as_view(),name="contratar_servicio_update"),
    path("contratar/delete/<int:pk>/", ContratarServicioDelete.as_view(),name="contratar_servicio_delete"),
    path("ofrecer/opinion/create/", OpinionServicioCreate.as_view(),name="ofrecer_servicio_opinion_create"),
    path("ofrecer/opiniones/<int:pk>/", OpinionServicioList.as_view(),name="ofrecer_servicio_opinion_list"),
]
