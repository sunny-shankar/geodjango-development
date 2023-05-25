from django.contrib import admin

from django.contrib.gis.admin import OSMGeoAdmin
from geo.models import GeoLocations

from leaflet.admin import LeafletGeoAdmin


@admin.register(GeoLocations)
class AdminView(LeafletGeoAdmin):
    list_display = ("location", "name")
