import requests
from django.views.generic import TemplateView
# Create your views here.
class BaseView(TemplateView):
    def dispatch(self, request, *args, **kwargs):
        self.meta = request.META
        print(self.meta)
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        r = requests.get("http://" + self.meta["HTTP_HOST"] + "/studysafe-core/api/hku-members/" + kwargs["uid"])
        context["user_found"] = (lambda x: x == 200)(r.status_code)
        if context["user_found"]:
            self.result = r.json()
            context["subject"] = self.result["name"]
        return context

class ContactsView(BaseView):
    template_name = "contacts.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if context["user_found"]:
            # add contacts logic
            print(self.result)
            pass
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