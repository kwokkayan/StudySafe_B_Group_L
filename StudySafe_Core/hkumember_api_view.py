from rest_framework import viewsets
from rest_framework.response import Response
from .models import HKUMember
from .hkumember_serializer import HKUMemberSerializer
# test code
# fetch(".", {method:"DELETE", headers: {'X-CSRFToken': csrftoken, 'content-type': 'application/json'}}).then(r => {console.log(r)})
class HKUMemberViewSet(viewsets.ModelViewSet):
    queryset = HKUMember.objects.all()
    serializer_class = HKUMemberSerializer