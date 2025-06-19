from django.urls import path, include
from rest_framework.routers import DefaultRouter
from vehicles.views import VehicleViewSet, VehicleTypeViewSet

router = DefaultRouter()
router.register(r'vehicles/type', VehicleTypeViewSet)  # registrando a rota para o ViewSet
router.register(r'vehicles', VehicleViewSet) 

urlpatterns = [
    path('', include(router.urls)),
]
