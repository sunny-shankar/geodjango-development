from django.contrib import admin

from django.contrib.gis.admin import OSMGeoAdmin
from geo.models import GeoLocations


@admin.register(GeoLocations)
class ShopAdmin(OSMGeoAdmin):
    list_display = ("location",)
