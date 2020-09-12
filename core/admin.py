from django.contrib import admin
from .models import ParkingSlot, Parking

# Register your models here.


@admin.register(ParkingSlot)
class ParkingSlotAdmin(admin.ModelAdmin):
    list_display = ('slot_number', 'is_available')


@admin.register(Parking)
class ParkingAdmin(admin.ModelAdmin):
    list_display = ('car_number', 'parking_slot', 'entry_time', 'exit_time', 'enabled')
