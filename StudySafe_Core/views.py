from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from .models import *
import json
# Create your views here.
#
# ISSUES: CHECKING JSON INPUT
#
#
class ViewAllHKUMembers(View):
    model = HKUMember
    def get(self, request, *args, **kwargs):
        members = self.model.objects.all()
        arr = []
        for member in members:
            arr.append({'name': member.name, 'uid': member.uid})
        return HttpResponse(json.dumps({"result": arr}), content_type="application/json")
    
    def http_method_not_allowed(self, request, *args, **kwargs):
        return HttpResponse("Method forbidden.")
# Test driver code:
# function getCookie(name) {
#     let cookieValue = null;
#     if (document.cookie && document.cookie !== '') {
#         const cookies = document.cookie.split(';');
#         for (let i = 0; i < cookies.length; i++) {
#             const cookie = cookies[i].trim();
#             // Does this cookie string begin with the name we want?
#             if (cookie.substring(0, name.length + 1) === (name + '=')) {
#                 cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
#                 break;
#             }
#         }
#     }
#     return cookieValue;
# }
# const csrftoken = getCookie('csrftoken');
# fetch("./create", {method:"POST", body:JSON.stringify({'name':'test1', 'uid':'3035705330'}), headers: {'X-CSRFToken': csrftoken, 'content-type': 'application/json'}}).then(r => {console.log(r)})
class CreateHKUMembers(View):
    model = HKUMember
    def post(self, request, *args, **kwargs):
        data = json.loads(request.body)
        try:
            name = data['name']
            uid = data['uid']
        except KeyError:
            return HttpResponse(code=400)
        member = self.model(name=name, uid=uid)
        output_message = member.save()
        return HttpResponse(output_message)

    def http_method_not_allowed(self, request, *args, **kwargs):
        return HttpResponse("Method forbidden.")

class SearchHKUMembersByName(View):
    model = HKUMember
    def get(self, request, *args, **kwargs):
        try:
            name = self.kwargs["name"]
        except KeyError:
            return HttpResponse(code=400)
        members = self.model.objects.all().filter(name=name)
        arr = []
        for member in members:
            arr.append({'name': member.name, 'uid': member.uid})
        return HttpResponse(json.dumps({"result": arr}), content_type="application/json")
    def http_method_not_allowed(self, request, *args, **kwargs):
        return HttpResponse("Method forbidden.")

class SearchHKUMembersByUid(View):
    model = HKUMember
    def get(self, request, *args, **kwargs):
        try:
            uid = self.kwargs["uid"]
        except KeyError:
            return HttpResponse(code=400)
        members = self.model.objects.all().filter(uid=uid)
        arr = []
        for member in members:
            arr.append({'name': member.name, 'uid': member.uid})
        return HttpResponse(json.dumps({"result": arr}), content_type="application/json")
    def http_method_not_allowed(self, request, *args, **kwargs):
        return HttpResponse("Method forbidden.")
# Test driver code:
# function getCookie(name) {
#     let cookieValue = null;
#     if (document.cookie && document.cookie !== '') {
#         const cookies = document.cookie.split(';');
#         for (let i = 0; i < cookies.length; i++) {
#             const cookie = cookies[i].trim();
#             // Does this cookie string begin with the name we want?
#             if (cookie.substring(0, name.length + 1) === (name + '=')) {
#                 cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
#                 break;
#             }
#         }
#     }
#     return cookieValue;
# }
# const csrftoken = getCookie('csrftoken');
# fetch("./modify", {method:"PUT", body:JSON.stringify({'target_uid':'3035705330', 'name':'test01'}), headers: {'X-CSRFToken': csrftoken, 'content-type': 'application/json'}}).then(r => {console.log(r)})
# cannot modify primary key
class ModifyHKUMembers(View):
    model = HKUMember
    def put(self, request, *args, **kwargs):
        data = json.loads(request.body)
        try:
            target_uid = data['target_uid']
        except KeyError:
            return HttpResponse(code=400)
        # must change at least one field
        name = None
        try:
            name = data['name']
        except KeyError:
            return HttpResponse(code=400)
        query_res = self.model.objects.all().filter(uid=target_uid)
        if len(query_res) != 1:
            return HttpResponse("HKU Member does not exists.")
        target_member = query_res[0]
        target_member.name = name
        output_message = target_member.save()
        return HttpResponse(output_message)
    def http_method_not_allowed(self, request, *args, **kwargs):
        return HttpResponse("Method forbidden.")
# Test driver code:
# function getCookie(name) {
#     let cookieValue = null;
#     if (document.cookie && document.cookie !== '') {
#         const cookies = document.cookie.split(';');
#         for (let i = 0; i < cookies.length; i++) {
#             const cookie = cookies[i].trim();
#             // Does this cookie string begin with the name we want?
#             if (cookie.substring(0, name.length + 1) === (name + '=')) {
#                 cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
#                 break;
#             }
#         }
#     }
#     return cookieValue;
# }
# const csrftoken = getCookie('csrftoken');
# fetch("./delete", {method:"DELETE", body:JSON.stringify({'uid':'3035705330', 'name':'test01'}), headers: {'X-CSRFToken': csrftoken, 'content-type': 'application/json'}}).then(r => {console.log(r)})
class DeleteHKUMembers(View):
    model = HKUMember
    def delete(self, request, *args, **kwargs):
        data = json.loads(request.body)
        try:
            uid = data['uid']
        except KeyError:
            return HttpResponse(code=400)
        query_res = self.model.objects.all().filter(uid=uid)
        if len(query_res) != 1:
            return HttpResponse("HKU Member does not exists.")
        member = query_res[0]
        member.delete() # idk about error handling
        return HttpResponse("HKU Member deleted.")

