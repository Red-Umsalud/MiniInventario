from django.urls import path
from .views import getActivoListAPIView, getActivoUbicacionListAPIView, getActivonombreListaAPIView

urlpatterns = [
    path('activos/', getActivoListAPIView, name='get_activo_list_api_view'),
    path('activo_ubicacion', getActivoUbicacionListAPIView, name='get_activo_ubicacion_list_api_view'),
    path('activo_nombre', getActivonombreListaAPIView, name='get_activo_nombre_list_api_view')
]
