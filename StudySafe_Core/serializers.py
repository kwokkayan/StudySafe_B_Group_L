from StudySafe_Core.models import Venues
from rest_framework import serializers

class VenueSerializer(serializers.ModelSerializer):
        
        class Meta:
                model = Venues
                fields = '__all__'