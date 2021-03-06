from rest_framework import filters
# from rest_framework.filters import SearchFilter 
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import Profile,ProfileStatus
from .serializers import ProfileSerializer,ProfileStatusSerializer,ProfileAvatarSerializer
# from rest_framework.viewsets import ReadOnlyModelViewSet
from rest_framework import viewsets
from rest_framework import mixins
from .permissions import IsOwnProfileOrReadOnly,IsOwnerOrReadOnly


# Create your views here.

class AvatarUpdateView(generics.UpdateAPIView):
    serializer_class=ProfileAvatarSerializer
    permission_classes=[IsAuthenticated]

    def get_object(self):
        profile_object=self.request.user.profile
        return profile_object

class ProfileViewSet(mixins.UpdateModelMixin,mixins.ListModelMixin,mixins.RetrieveModelMixin,viewsets.GenericViewSet):
    queryset=Profile.objects.all()
    serializer_class=ProfileSerializer
    permission_classes=[IsAuthenticated,IsOwnProfileOrReadOnly]
    filter_backends = [filters.SearchFilter]
    search_fields = ['city']
    #this city is same name in Profile model not differnt

class ProfileStatusViewSet(viewsets.ModelViewSet):
    
    serializer_class=ProfileStatusSerializer
    permission_classes=[IsAuthenticated,IsOwnerOrReadOnly]

    def get_queryset(self):
        queryset=ProfileStatus.objects.all()
        username=self.request.query_params.get("username",None)
        if(username is not None):
            queryset=queryset.filter(user_profile__user__username=username)
            #the filter argument meaning ProfileStatus model in that foriegn key user_profile in that Profile table user in that User Table Username
        return queryset
        

    def perform_create(self, serializer):
        user_profile=self.request.user.profile
        serializer.save(user_profile=user_profile)

