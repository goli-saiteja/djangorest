from .models import Users
from rest_framework import serializers


class UsersSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        password = validated_data.pop("password")
        user = Users.objects.create(**validated_data)
        if password:
           user.set_password(password)
           user.save()
        return user

    def update(self, instance, validated_data):
        password = validated_data.pop("password")
        instance.__dict__.update(validated_data)
        if password:
           instance.set_password(password)
        instance.save()
        return instance
    password = serializers.CharField(write_only=True)
    class Meta:
        model = Users
        fields = ('first_name', 'last_name', 'email','id' ,'password')
        read_only_fields = ('date_joined',)
