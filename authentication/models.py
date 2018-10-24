from django.db import models
from django.contrib.auth.models import AbstractBaseUser,UserManager

class Users(AbstractBaseUser):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30, blank=True)
    email = models.EmailField(unique=True)
    date_joined = models.DateTimeField(auto_now=True)
    objects = UserManager()
    USERNAME_FIELD = 'first_name'
    REQUIRED_FIELDS = ['email']

    class Meta:
        db_table = "chat_users"
