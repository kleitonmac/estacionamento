from django.contrib import admin
from vehicles.models import VehicleType, Vehicle

@admin.register(VehicleType)
class VehicleTypeAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'create_at', 'update_at']
    search_fields = ['name']
    ordering = ['name']


@admin.register(Vehicle)
class VehicleAdmin(admin.ModelAdmin):
    list_display = ['vehicle_type', 'brand', 'model', 'license_plate', 'color', 'owner', 'create_at']
    search_fields = ['model', 'license_plate', 'brand']
    list_filter = ['vehicle_type', 'brand', 'color']
    ordering = ['vehicle_type', 'brand']
