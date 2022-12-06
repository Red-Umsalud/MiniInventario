from rest_framework.decorators import api_view
from rest_framework.response import Response
from app.models import Activo, Fotografia
from .serializers import ActivoSerializer, FotografiaSerializer
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
def getActivoNombreListAPIView(request):
    activos = Activo.objects.filter(nombre__contains=request.GET['nombre'])
    serializer = ActivoSerializer(activos, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getActivoCodigoListAPIView(request):
    activos = Activo.objects.filter(codigo__contains=request.GET['codigo'])
    serializer = ActivoSerializer(activos, many=True)
    return Response(serializer.data)
    
@api_view(['GET'])
def getActivoDescripcionListAPIView(request):
    activos = Activo.objects.filter(descripcion__contains=request.GET['descripcion'])
    serializer = ActivoSerializer(activos, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getActivoFotografiaListAPIView(request):
    fotografias = Fotografia.objects.filter(id_activo=request.GET['id_activo'])
    serializer = FotografiaSerializer(fotografias, many=True)
    return Response(serializer.data)