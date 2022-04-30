import requests
from datetime import datetime 
from django.views.generic import TemplateView
# Create your views here.
class BaseView(TemplateView):
    def dispatch(self, request, *args, **kwargs):
        self.meta = request.META
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        hku_members = requests.get("http://" + self.meta["HTTP_HOST"] + "/studysafe-core/api/hku-members/" + kwargs["uid"] + "/")
        travel_records = requests.get("http://" + self.meta["HTTP_HOST"] + "/studysafe-core/api/travel-records/")
        context["user_found"] = (lambda x: x == 200)(hku_members.status_code)
        context["travel_records_found"] = (lambda x: x == 200)(travel_records.status_code)
        if context["user_found"]:
            self.result = hku_members.json()
            context["subject"] = self.result["name"]
            if context["travel_records_found"]:
                self.travel_records = travel_records.json()
        return context

class ContactsView(BaseView):
    template_name = "contacts.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if context["user_found"]:
            # add venues logic
            visited = self.result["visited"]
            context["contacts"] = []
            for user_visited in visited:
                for other_visited in  self.travel_records:
                    if user_visited["time_of_exit"] is None or other_visited["time_of_exit"] is None:
                        continue
                    if user_visited["uid"] == other_visited["uid"]:
                        continue
                    user_entry = datetime.fromisoformat(user_visited["time_of_entry"])
                    user_exit = datetime.fromisoformat(user_visited["time_of_exit"])
                    other_entry = datetime.fromisoformat(other_visited["time_of_entry"])
                    other_exit = datetime.fromisoformat(other_visited["time_of_exit"])
                    # check for overlap
                    if (user_entry >= other_entry and user_entry <= other_exit) or (other_entry >= user_entry and other_entry <= user_exit): 
                        dt = min(user_exit, other_exit) - max(user_entry, other_entry)
                        print(user_visited["id"], other_visited["id"])
                        print("dt1 =", dt)
                        if (dt.total_seconds() > 1800): # 30 mins overlap
                            if other_visited["uid"] not in context["contacts"]: # only unique
                                context["contacts"].append(other_visited["uid"])
            context["contacts"].sort()
        return context

class VenuesView(BaseView):
    template_name = "venues.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if context["user_found"]:
            # add venues logic
            print(self.result)
            pass
        return context