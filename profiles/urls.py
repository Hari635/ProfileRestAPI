from django.urls import path,include
from .views import ProfileViewSet,ProfileStatusViewSet,AvatarUpdateView
from rest_framework.routers import DefaultRouter
# profile_list=ProfileViewSet.as_view({"get":"list"})
# profile_detail=ProfileViewSet.as_view({"get":"retrieve"})
#if you using viewset then use router module for url 
router=DefaultRouter()
router.register(r"profiles",ProfileViewSet)
router.register(r"status",ProfileStatusViewSet,basename="status")


urlpatterns=[
    path("",include(router.urls)),
    path("avatar/",AvatarUpdateView.as_view(),name="avatar-update")
   
]