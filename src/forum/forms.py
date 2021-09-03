from django import forms
from django.db import transaction
from ckeditor.widgets import CKEditorWidget

from forum.models import Message, Topic


class TopicForm(forms.Form):
    name = forms.CharField(max_length=255)
    text = forms.CharField(widget=CKEditorWidget())

    @transaction.atomic
    def save(self, section, author) -> Topic:
        topic = Topic.objects.create(section=section, author=author, name=self.cleaned_data['name'])
        message = Message.objects.create(topic=topic, author=author, text=self.cleaned_data['text'])
        return topic


class MessageForm(forms.ModelForm):

    class Meta:
        model = Message
        fields = ('text',)
