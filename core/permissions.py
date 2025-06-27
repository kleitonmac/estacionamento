from rest_framework import permissions

class IsOwnerOfVehiclesOrRecord(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        user = request.user

        # Verifica se o objeto tem um atributo 'owner'
        if hasattr(obj, 'owner') and hasattr(obj.owner, 'user'):
            return obj.owner.user == user

        # Verifica se o objeto tem um atributo 'vehicle' e se vehicle possui 'owner'
        if hasattr(obj, 'vehicle') and hasattr(obj.vehicle, 'owner') and hasattr(obj.vehicle.owner, 'user'):
            return obj.vehicle.owner.user == user

        return False

   

       