from django import forms
from django.forms import fields

from forum.models import Message


class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ('text',)
