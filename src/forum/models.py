from django.contrib import admin
from django.db import models
from django.urls import reverse
from django.conf import settings


class Section(models.Model):
    name = models.CharField(max_length=120)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')

    def __str__(self) -> str:
        return self.name

    def get_absolute_url(self):
        return reverse("section", kwargs={"pk": self.pk})
    
    @admin.display(boolean=True, ordering='parent')
    def is_top_section(self) -> bool:
        return not self.parent

    def get_last_message(self):
        return Message.objects.filter(topic__in=self.topics.all()).order_by('-created_at').first()


class Topic(models.Model):
    section = models.ForeignKey(Section, on_delete=models.CASCADE, null=False, blank=False, related_name='topics')
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=False, blank=False, related_name='topics')
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    is_closed = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.name

    def get_absolute_url(self):
        return reverse("topic", kwargs={"pk": self.pk})

    def get_last_message(self):
        return self.messages.order_by('-created_at').first()


class Message(models.Model):
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE, null=False, blank=False, related_name='messages')
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=False, blank=False, related_name='messages')
    text = models.TextField(blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
