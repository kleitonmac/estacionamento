from django.contrib import admin
from parking.models import ParkingSpot, ParkingRecord

@admin.register(ParkingSpot)
class ParkingSpotAdmin(admin.ModelAdmin):
    list_display = ['spot_number', 'is_occupied']  # Corrigido aqui
    search_fields = ['spot_number']                # Corrigido aqui
    list_filter = ['is_occupied']

@admin.register(ParkingRecord)
class ParkingRecordAdmin(admin.ModelAdmin):
    list_display = ['vehicle', 'parking_spot', 'entry_time', 'exit_time']
    search_fields = ['vehicle__license_plate', 'parking_spot__spot_number']
