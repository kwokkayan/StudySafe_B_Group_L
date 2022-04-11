from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from .models import *
import json
# Create your views here.
class ViewAllHKUMembers(View):
    model = HKUMember
    def get(self, request, *args, **kwargs):
        members = self.model.objects.all()
        arr = []
        for member in members:
            arr.append({'name': member.name, 'uid': member.uid})
        return HttpResponse(json.dumps({"result": arr}), content_type="application/json")