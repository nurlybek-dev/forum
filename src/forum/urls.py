from django.urls import path, include

from .views import index, section, topic


urlpatterns = [
    path("", index, name="index"),
    path("section/<int:pk>/", section, name="section"),
    path("topic/<int:pk>/", topic, name="topic"),
]
