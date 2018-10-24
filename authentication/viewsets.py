from .models import Users
from rest_framework import viewsets, permissions
from .serializers import UsersSerializer
from django.contrib.auth.hashers import make_password

class UsersViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Users.objects.all().order_by('-date_joined')
    serializer_class = UsersSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def populate(self, request, context, mode):
        if 'password' in context.keys():
            context.update({'password': make_password(context['password']) })
