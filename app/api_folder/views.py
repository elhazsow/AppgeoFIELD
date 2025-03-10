from rest_framework import viewsets
from rest_framework_gis import filters

from app.models import ZonesProtgesDuSngal
from .serializers import (
    ZonesProtgesDuSngal_Serializer,
) 


class ZonesProtgesDuSngal_Api_ViewSet(
    viewsets.ReadOnlyModelViewSet,
):
    bbox_filter_field = "geom"
    filter_backends = [filters.InBBoxFilter] #on charge seulement les features dans bbox
    queryset = ZonesProtgesDuSngal.objects.all()
    serializer_class = ZonesProtgesDuSngal_Serializer
    