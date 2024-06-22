from django.urls import path
from .views import index, info, portafolio, patreon, registro, referencia

urlpatterns = [
    path('index', index, name="index"),
    path('index/info', info, name="info"),
    path('index/portafolio', portafolio, name="portafolio"),
    path('index/patreon', patreon, name="patreon"),
    path('index/registro', registro, name="registro"),
    path('index/referencia', referencia, name="referencia")
]