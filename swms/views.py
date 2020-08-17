from rest_framework import viewsets, permissions, filters
from django_filters import rest_framework as dj_filters
from .models import Reservoir
from .serializers import ReservoirSerializer
from .pagination import StandardResultsSetPagination


class ReservoirViewset(viewsets.ModelViewSet):
    queryset = Reservoir.objects.all()
    serializer_class = ReservoirSerializer
    # permission_classes = [permissions.IsAuthenticated]
    pagination_class = StandardResultsSetPagination
    search_fields = ["name", "division"]
    filterset_fields = ["division"]
    ordering_fields = ["name", "division",
                       "capacity", "catchment_area", "surface_area"]
