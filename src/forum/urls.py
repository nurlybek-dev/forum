from django.urls import path, include

from .views import index, message_create, section, topic, topic_create


urlpatterns = [
    path("", index, name="index"),
    path("section/<int:pk>/", section, name="section"),
    path("section/<int:section>/create_topic/", topic_create, name="topic-create"),
    path("topic/<int:pk>/", topic, name="topic"),
    path("topic/<int:topic>/create_message/", message_create, name="message-create"),
]
