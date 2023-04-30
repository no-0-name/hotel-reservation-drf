from django.urls import re_path

from . import views


urlpatterns = [
    re_path(r"(?P<api_name>[a-z]+)", views.listView, name="hotel_api")
]
