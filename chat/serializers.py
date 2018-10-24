from rest_framework import serializers
from .models import Message

class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ("created_by", "recipient", "message_body", "created_date", "parent", "status")
