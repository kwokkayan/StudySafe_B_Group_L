from rest_framework import serializers
from .models import HKUMember, TravelRecord

class TravelRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = TravelRecord
        fields = '__all__'

class HKUMemberSerializer(serializers.ModelSerializer):
    visited = TravelRecordSerializer(many=True, read_only=True)
    class Meta:
        model = HKUMember
        fields = '__all__'
