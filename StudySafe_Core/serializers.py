from .models import *
from rest_framework import serializers

class VenueSerializer(serializers.ModelSerializer):
    class Meta:
        model = Venue
        fields = '__all__'
                
class TravelRecordSerializer(serializers.ModelSerializer):
    def validate(self, data):
        if data["time_of_exit"] is not None and data["time_of_entry"] > data["time_of_exit"]:
            raise serializers.ValidationError("Time of Exit cannot be earlier than Time of Entry")
        return data
    class Meta:
        model = TravelRecord
        fields = '__all__'

class HKUMemberSerializer(serializers.ModelSerializer):
    visited = TravelRecordSerializer(many=True, read_only=True)
    class Meta:
        model = HKUMember
        fields = '__all__'