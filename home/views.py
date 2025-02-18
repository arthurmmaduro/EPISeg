from django.shortcuts import render
from colaboradores.models import Colaborador

# Create your views here.

def home(request):
    try:
        colaborador = Colaborador.objects.get(usuario=request.user)
    except Colaborador.DoesNotExist:
        colaborador = None
    return render(request, 'home/home.html', {'colaborador': colaborador})