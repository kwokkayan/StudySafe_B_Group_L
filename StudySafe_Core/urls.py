from django.urls import path
from StudySafe_Core import views

urlpatterns = [
    path('hkumembers/listall', views.ViewAllHKUMembers.as_view(), name="view-all-HKUMembers"),
    path('hkumembers/create', views.CreateHKUMembers.as_view(), name="create-HKUMembers"),
    path('hkumembers/searchbyname/<str:name>', views.SearchHKUMembersByName.as_view(), name="search-by-name-HKUMembers"),
    path('hkumembers/searchbyuid/<int:uid>', views.SearchHKUMembersByUid.as_view(), name="search-by-uid-HKUMembers"),
    path('hkumembers/modify', views.ModifyHKUMembers.as_view(), name="modify-HKUMembers"),
    path('hkumembers/delete', views.DeleteHKUMembers.as_view(), name="delete-HKUMembers")
]