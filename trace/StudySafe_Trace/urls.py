from django.urls import re_path, path, register_converter
from .views import ContactsView, VenuesView;
from .converter import DateConverter, UIDConverter

register_converter(DateConverter, 'date')
register_converter(UIDConverter, 'uid')

urlpatterns = [
    path('contacts/<uid:uid>/<date:date>', ContactsView.as_view(), name='contacts'),
    path('venues/<uid:uid>/<date:date>', VenuesView.as_view(), name='venues')
]