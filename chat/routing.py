from django.urls import re_path
from .consumers import ChatConsumer
from . import consumers

# websocket URL → consumer
websocket_urlpatterns = [
     re_path(r"ws/chat/(?P<room_name>[^/]+)/$", consumers.ChatConsumer.as_asgi()),
]