from django.contrib.auth import get_user_model
from rest_framework import viewsets
from user.api.serializers import UserSerializer
from rest_framework.permissions import AllowAny


class UserViewSet(viewsets.ModelViewSet):
    queryset = get_user_model().objects
    serializer_class = UserSerializer
    http_method_names = ['post']

    def get_permissions(self):
        if self.request.method == 'POST':
            self.permission_classes = (AllowAny,)
        return super(UserViewSet, self).get_permissions()
