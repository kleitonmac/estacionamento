from rest_framework.permissions import DjangoModelPermissions, IsAdminUser
from rest_framework import viewsets
from core.permissions import IsOwnerOfVehiclesOrRecord
from vehicles.models import Vehicle , VehicleType
from vehicles.serializers import VehicleSerializer, VehicleTypeSerializer

class VehicleViewSet(viewsets.ModelViewSet):
    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializer
    permission_classes = [DjangoModelPermissions, IsOwnerOfVehiclesOrRecord] # Estou permitindo a covifuracao de usaria feita http://127.0.0.1:8000/admin

class VehicleTypeViewSet(viewsets.ModelViewSet):
    queryset = VehicleType.objects.all()
    serializer_class = VehicleTypeSerializer
    permission_classes = [DjangoModelPermissions , IsAdminUser] 
    
    def get_queryset(self):
        user = self.request.user
        if user.is_staff:
            return Vehicle.objects.all()
        return Vehicle.objects.filter(owner__user=user)
