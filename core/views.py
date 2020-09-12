from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.core.serializers import serialize
from .models import Parking, ParkingSlot
from django.conf import settings
from datetime import datetime


# Create your views here.
def parking_car(request):
    if request.method == 'GET':
        return JsonResponse({'status': 204, 'msg': 'Method Not Allowed'})
    available_slot_count = ParkingSlot.objects.filter(is_available=True).count()
    parked_cnt = Parking.objects.filter(enabled=True).count()
    if parked_cnt >= int(settings.PARKING_LOT_SIZE) or available_slot_count == 0:
        return JsonResponse({'status': 204, 'msg': "There isn't available parking slot"})

    number = request.POST.get('number', None)
    parking_slot = ParkingSlot.objects.filter(is_available=True).first()
    if number is None or parking_slot is None:
        return JsonResponse({'status': 204, 'msg': "Please fill the required fields."})
    parking = Parking.objects.create(
        car_number=number,
        parking_slot=parking_slot
    )
    parking.save()

    return JsonResponse({
        'status': 200,
        'msg': 'Successfully parked',
        'parking': {
            "parking_slot": parking.parking_slot.slot_number,
            "car_number": parking.car_number,
            "entry_time": parking.entry_time
        }
    })


def unparking_car(request):
    if request.method == 'GET':
        return JsonResponse({'status': 204, 'msg': 'Method Not Allowed'})

    slot_number = request.POST.get('slot_number')
    slot = ParkingSlot.objects.filter(slot_number=slot_number).first()
    parking = slot.parkings.filter(enabled=True).first()
    parking.exit_time = datetime.now()
    parking.enabled = False
    parking.save()
    return JsonResponse({
        'status': 200,
        'msg': 'Successfully Unparked'
    })


def parking_information(request):
    number = request.GET.get('number', None)
    slot_number = request.GET.get('slot_number', None)
    parking = None
    if slot_number:
        parking = Parking.objects.filter(parking_slot__slot_number=slot_number, enabled=True).first()
        # slot = ParkingSlot.objects.filter(slot_number=slot_number).first()
        # parking = slot.parkings.filter(enabled=True).first()
    elif number:
        parking = Parking.objects.filter(enabled=True).first()

    if parking is None:
        return JsonResponse({'status': 204, 'msg': 'Can not find parking slot'})

    return JsonResponse({
        'status': 200,
        'parking': {
            "parking_slot": parking.parking_slot.slot_number,
            "car_number": parking.car_number,
            "entry_time": parking.entry_time
        }
    })

