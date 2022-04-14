from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .api_views import VenueViewSet

router = DefaultRouter()
router.register(r'venues', VenueViewSet, 'venue')

urlpatterns = [
        path('api/', include(router.urls)),
]