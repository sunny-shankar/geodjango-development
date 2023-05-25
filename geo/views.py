from django.shortcuts import render
from geo.models import GeoLocations
from django.http import HttpResponse
from geopy.geocoders import Nominatim
from django.contrib.gis.geos import Point
from django.core.serializers import serialize
import requests

geolocator = Nominatim(user_agent="GetLoc")


def insert_data(requests):
    if requests.method == "POST":
        address = requests.POST.get("address")
        if not address:
            return HttpResponse("Required Address")
        location = get_location(address)
        print(location.latitude, location.longitude)
        print(
            GeoLocations.objects.create(
                name=location.address,
                location=Point(location.latitude, location.longitude),
            )
        )

    return render(requests, "form.html", {})


def home_view(requests):
    results = []
    objects = GeoLocations.objects.all()

    for obj in objects:
        latitude, longitude = obj.location.coords

        results.append(
            {
                "name": obj.name,
                "latitude": latitude,
                "longitude": longitude,
                "forecast": get_forecast(latitude, longitude),
            }
        )
    return render(requests, "index.html", {"results": results})


def get_location(addrs):
    location = geolocator.geocode(addrs)
    return location


def get_forecast(latitude, longitude):
    url = f"https://api.weather.gov/points/{latitude},{longitude}"

    response = requests.request("GET", url)

    data = response.json()
    if response.status_code == 200:
        forecast_url = data["properties"]["forecast"]
        forecast_data = requests.request("GET", forecast_url).json()
        if forecast_data.get("properties"):
            return forecast_data["properties"]["periods"][0]
