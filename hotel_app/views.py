from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from collections import namedtuple

from .models import Customer, Hotel, Room, Booking
from .serializer import CustomerSerializer, HotelSerializer, RoomSerializer, BookingSerializer


named_tuple = namedtuple("object", ["model", "serializers"])

hotel_objects = {
    "customer"  : named_tuple(Customer, CustomerSerializer),
    "hotel"  : named_tuple(Hotel, HotelSerializer),
    "room"   : named_tuple(Room, RoomSerializer),
    "booking": named_tuple(Booking, BookingSerializer),
}

@api_view(["GET", "POST"])
def listView(request, api_name):
    object = hotel_objects.get(api_name, None)
    
    if request.method == "GET":
        object_list = object.model.objects.all()
        serializers = object.serializers(object_list, many=True)
        return Response(serializers.data)
    
    elif request.method == "POST":
        serializers = object.serializers(data=request.data)

        if serializers.is_valid():
            serializers.save()
            return Response(
                data = serializers.data,
                status = status.HTTP_201_CREATED
            )
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)