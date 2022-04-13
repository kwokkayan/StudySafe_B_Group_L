from rest_framework import serializers
from .models import HKUMember
class HKUMemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = HKUMember
        fields = '__all__'