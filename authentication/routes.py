from django.conf.urls import include, url

from rest_framework.routers import DefaultRouter

from .viewsets import UsersViewSet

router = DefaultRouter()
router.register(r'users', UsersViewSet,
                base_name="users_list")

urlpatterns = [
    url(r'^', include(router.urls)),
]
