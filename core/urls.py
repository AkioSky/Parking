from django.urls import path
from . import views


app_name = 'core'

urlpatterns = [
    path('parking/', views.parking_car, name='parking'),
    path('unparking/', views.unparking_car, name='unparking'),
    path('parking-info/', views.parking_information, name='information')
]