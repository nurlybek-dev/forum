from django import forms
from django.contrib.auth import forms as auth_forms

from .models import User

class UserCreationForm(auth_forms.UserCreationForm):

    class Meta(auth_forms.UserCreationForm):
        model = User
        fields = ("username", "email",)


class UserChangeForm(auth_forms.UserChangeForm):

    class Meta:
        model = User
        fields = ('username', 'email', )


class EditProfileForm(forms.ModelForm):
    
    class Meta:
        model = User
        fields = ("first_name", "last_name", "email", )
