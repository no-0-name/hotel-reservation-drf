from django.contrib import admin

from .models import Customer, Hotel, Room, Booking


class CustomerAdmin(admin.ModelAdmin):
    list_display = ["name", "phone", "email"]
admin.site.register(Customer, CustomerAdmin)


class HotelAdmin(admin.ModelAdmin):
    list_display = ["name", "phone", "email", "location"]
admin.site.register(Hotel, HotelAdmin)


class RoomAdmin(admin.ModelAdmin):
    list_display = ["hotel", "room_num", "price", "is_booked"]
    list_editable = ["room_num", "price", "is_booked"]
admin.site.register(Room, RoomAdmin)


class BookingAdmin(admin.ModelAdmin):
    list_display = ["customer", "hotel", "room", "checkout_date", "is_checkout"]
    list_editable = ["checkout_date", "is_checkout"]
    list_filter = ["checkout_date"]
admin.site.register(Booking, BookingAdmin)