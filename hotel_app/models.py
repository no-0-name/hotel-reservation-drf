from django.db import models
from datetime import datetime


class Customer(models.Model):
    name = models.CharField(max_length=20)
    phone = models.CharField(max_length=20)
    email = models.EmailField(max_length=60)

    class Meta:
        verbose_name = "Customer"
        verbose_name_plural = "Customers"


class Hotel(models.Model):
    name = models.CharField(max_length=20)
    phone = models.CharField(max_length=20)
    email = models.EmailField(max_length=60)
    location = models.CharField(max_length=60)

    class Meta:
        verbose_name = "Hotel"
        verbose_name_plural = "Hotels"


class Room(models.Model):
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    room_num = models.IntegerField(default=100)
    price = models.FloatField(default=100.0)
    is_booked = models.BooleanField(default=False)
    
    class Meta:
        verbose_name = "Room"
        verbose_name_plural = "Rooms"


class Booking(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    checkout_date = models.DateField(default=datetime.now)
    is_checkout = models.BooleanField(default=False)
