from email.policy import default
import imp
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from StudySafe_Core import views, hkumember_api_view

router = DefaultRouter()
router.register(r'hkumembers', hkumember_api_view.ViewAllHKUMembers, 'view-all-HKUMembers')

urlpatterns = [
    path('api/', include(router.urls))
]