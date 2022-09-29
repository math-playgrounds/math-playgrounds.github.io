from django.urls import re_path

from . import consumers

websocket_urlpatterns = [
    re_path(r'ws/polls/(?P<room_name>\w+)/$',
            consumers.PollsConsumer.as_asgi()),
]
