from django.shortcuts import render

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
    return render(request, 'web/registro.html')