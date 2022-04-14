from rest_framework import viewsets
from .models import Venues
from .serializers import VenueSerializer


class VenueViewSet(viewsets.ModelViewSet):
        queryset = Venues.objects.all()
        serializer_class = VenueSerializer
        