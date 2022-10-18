from rest_framework.decorators import api_view
from rest_framework.response import Response
from app.models import Activo
from .serializers import ActivoSerializer 
# Create your views here.

@api_view(['GET'])
def getActivoListAPIView(request):
    activos = Activo.objects.all()
    serializer = ActivoSerializer(activos, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getActivoUbicacionListAPIView(request):
    activos = Activo.objects.filter(ubicacion__contains=request.GET['ubicacion'])
    serializer = ActivoSerializer(activos, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getActivonombreListaAPIView(request):
    activos = Activo.objects.filter(nombre__contains=request.GET['nombre'])
    serializer = ActivoSerializer(activos, many=True)
    return Response(serializer.data)
