from django.urls import path, include
from rest_framework.routers import DefaultRouter
from StudySafe_Core.api_views import *
from django.views.generic import TemplateView

router = DefaultRouter()
router.register(r'hku-members', HKUMemberViewSet, 'HKU Members')
router.register(r'travel-records', TravelRecordViewSet, 'Travel Records')
router.register(r'venues', VenueViewSet, 'venue')
urlpatterns = [
    path('api/', include(router.urls)),
    path('api/docs', TemplateView.as_view(template_name="doc.html"), name='documentation')
]