from rest_framework import viewsets
from rest_framework.response import Response
from .models import HKUMember, TravelRecord
from .serializer import HKUMemberSerializer, TravelRecordSerializer
# test code
# fetch(".", {method:"DELETE", headers: {'X-CSRFToken': csrftoken, 'content-type': 'application/json'}}).then(r => {console.log(r)})
class HKUMemberViewSet(viewsets.ModelViewSet):
    queryset = HKUMember.objects.all()
    serializer_class = HKUMemberSerializer

class TravelRecordViewSet(viewsets.ModelViewSet):
    queryset = TravelRecord.objects.all()
    serializer_class = TravelRecordSerializer