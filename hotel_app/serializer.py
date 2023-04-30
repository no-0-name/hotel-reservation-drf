from rest_framework import fields, serializers

from .models import Customer, Hotel, Room, Booking


class CustomerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Customer
        fields = ("name", "phone", "email")


class HotelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hotel
        fields = ("name", "phone", "email", "location")


class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = ("hotel", "room_num", "price", "is_booked")


class BookingSerializer(serializers.ModelSerializer):
    customer = CustomerSerializer
    hotel = HotelSerializer
    room = RoomSerializer
    
    class Meta:
        model = Booking
        fields = ("customer", "hotel", "room", "checkout_date", "is_checkout")