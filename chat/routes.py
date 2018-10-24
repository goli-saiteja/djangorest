from django.conf.urls import include, url
from rest_framework.routers import DefaultRouter
from .viewsets import MessageViewSet

router = DefaultRouter()
router.register(r'message', MessageViewSet, base_name ="messages_list")


urlpatterns =[
    url(r'^', include(router.urls)),
]
