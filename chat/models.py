from django.db import models
from authentication.models import Users
# Create your models here.
class Message(models.Model):
    created_by = models.ForeignKey(Users, related_name="created_by_id")
    recipient = models.ForeignKey(Users, related_name="recipient_id")
    message_body = models.TextField()
    created_date = models.DateTimeField(auto_now=True)
    parent = models.ForeignKey('self', blank=True,null=True, related_name='parent_message')
    status = models.CharField(max_length = 30, help_text = "Message status")
    class Meta:
        db_table = "chat_message"
