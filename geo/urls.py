from django.urls import path
from geo.views import home_view, insert_data

urlpatterns = [
    path("", home_view),
    path("add/", insert_data),
]
