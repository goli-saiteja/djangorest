from django.conf.urls import url, include
from authentication import routes as authentication_routes
from chat import routes as chat_routes
# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r'^api/authentication/', include(authentication_routes)),
    url(r'^api/chat/', include(chat_routes)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
