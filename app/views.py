from django.shortcuts import render
from .models import Fotografia, Activo
# Create your views here.
def main(request):
    activos = Activo.objects.all()
    #activos = Activo.objects.filter(ubicacion='Depósito 6')
    return render(request,'index.html',{'activos':activos})
