from rest_framework import permissions

class IsOwnProfileOrReadOnly(permissions.BasePermission):
    
    def has_object_permission(self, request, view, obj):
        # print("request name",request.user)
        # print("---")
        # print("obj name",obj.user)
        if(request.method in permissions.SAFE_METHODS):
            return True
        return obj.user==request.user

class IsOwnerOrReadOnly(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        # print(request.user.profile)
        # print("---")
        # print(obj.user_profile)
        if(request.method in permissions.SAFE_METHODS):
            return True
        return obj.user_profile==request.user.profile