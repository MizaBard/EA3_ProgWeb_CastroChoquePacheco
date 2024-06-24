from django.urls import path
from django.contrib.auth import views as auth_views
from .views import index, info, portafolio, patreon, registro, referencia, login

urlpatterns = [
    path('index', index, name="index"),
    path('index/info', info, name="info"),
    path('index/portafolio', portafolio, name="portafolio"),
    path('index/patreon', patreon, name="patreon"),
    path('index/registro', registro, name="registro"),
    path('index/referencia', referencia, name="referencia"),
    path('registration/login', login, name="login"),
    path('logout/', auth_views.LogoutView.as_view(next_page='/'), name='logout'),
]