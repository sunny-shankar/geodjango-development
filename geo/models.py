from django.contrib.gis.db import models
from django.contrib.gis.geos import Point
from uuid import uuid4


class BaseModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4())
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class GeoLocations(BaseModel):
    location = models.PointField(geography=True, default=Point(0.0, 0.0))
