from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from authentication.models import Users
from .models import Message
from .serializers import MessageSerializer

class MessageViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer

    def perform_create(self,serializer):
        serializer.save(created_by = Users.objects.get(id=self.request.data['created_by']), recipient = Users.objects.get(id = self.request.data['recipient']))
