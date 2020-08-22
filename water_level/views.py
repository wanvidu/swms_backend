from rest_framework import viewsets, permissions, filters
from django_filters import rest_framework as dj_filters
from .models import WaterLevel
from .serializers import WaterLevelSerializer
from .pagination import StandardResultsSetPagination
from .filters import WaterLevelFilter


class WaterLevelViewset(viewsets.ModelViewSet):
    queryset = WaterLevel.objects.all()
    serializer_class = WaterLevelSerializer
    # permission_classes = [permissions.IsAuthenticated]
    pagination_class = StandardResultsSetPagination
    filter_class = WaterLevelFilter
    search_fields = ["reservoir__name"]
    # filterset_fields = ["reservoir__name", "reservoir__id"]
    ordering_fie_lds = ["reservoir__name", "date", "water_level",
                        "water_consumption", "rainfall", "temperature", "evaporation"]
