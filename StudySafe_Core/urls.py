from django.urls import path
from StudySafe_Core import views

urlpatterns = [
    path('hkumembers/listall', views.ViewAllHKUMembers.as_view(), name="view-all-HKUMembers")
]