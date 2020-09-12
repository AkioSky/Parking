from django.db import models

# Create your models here.


class ParkingSlot(models.Model):
    slot_number = models.PositiveSmallIntegerField(unique=True)
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return "{}".format(self.slot_number)


# class Customer(models.Model):
#     customer_name = models.CharField(max_length=100)
#     car_number = models.CharField(max_length=10)
#     contact_number = models.CharField(max_length=12)


class Parking(models.Model):
    # customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    parking_slot = models.ForeignKey(ParkingSlot, on_delete=models.CASCADE, related_name='parkings')
    car_number = models.CharField(max_length=10)
    # parking_slot = models.PositiveSmallIntegerField()
    entry_time = models.DateTimeField(auto_now_add=True)
    exit_time = models.DateTimeField(blank=True, null=True)
    cost = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    enabled = models.BooleanField(default=True)

    def save(self, *args, **kwargs):
        if self.enabled:
            self.parking_slot.is_available = False
            self.parking_slot.save()
        else:
            self.parking_slot.is_available = True
            self.parking_slot.save()
        super(Parking, self).save(*args, **kwargs)
