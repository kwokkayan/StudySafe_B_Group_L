from email.policy import default
import imp
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from StudySafe_Core import views, hkumember_api_view
from django.views.generic import TemplateView

router = DefaultRouter()
router.register(r'hkumembers', hkumember_api_view.HKUMemberViewSet, 'view-all-HKUMembers')

urlpatterns = [
    path('api/', include(router.urls)),
    path('api/docs/hkumembers', TemplateView.as_view(template_name="hkumembers.html"), name='hkumembers-documentation')
]