from django.shortcuts import render
from .models import Usuario

# Create your views here.

def index(request):
    return render(request, 'web/index.html')

def info(request):
    return render(request, 'web/infoChan.html')

def portafolio(request):
    return render(request, 'web/portfolio.html')

def patreon(request):
    return render(request, 'web/patreon.html')

def registro(request):
    if request.method != "post":
        usuario=Usuario.objects.all()
        context={ 'usuario' : usuario }
        return render(request, 'web/registro.html') 
    else: 
        rut=request.post["rut"]
        nombre=request.post["nombre"]
        email=request.post["email"]
        contraseña=request.post["contraseña"] 
        telefono=request.post["telefono"]

        usuario=Usuario.objects.create(rut=rut, nombre=nombre, email=email, contraseña=contraseña, telefono=telefono)
        usuario.save()
        return render(request, 'web/registro.html')   
    
def referencia(request):
    return render(request, 'web/BrutalismoAPI.html')

