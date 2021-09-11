from django.contrib.auth.forms import PasswordChangeForm
from django.urls import reverse_lazy
from django.views.generic.edit import FormView
from django.views.generic import DetailView

from .models import User
from .forms import UserChangeForm, UserCreationForm


class SignupView(FormView):
    form_class = UserCreationForm
    template_name = 'registration/signup.html'
    success_url = reverse_lazy('login')

    def form_valid(self, form: UserCreationForm):
        form.save()
        return super().form_valid(form)


class ProfileView(DetailView):
    model = User
    template_name = 'users/profile.html'
    context_object_name = 'profile'


class EditProfileView(FormView):
    form_class = UserChangeForm
    template_name = 'users/edit_profile.html'
    context_object_name = 'profile'

    def form_valid(self, form: UserChangeForm):
        form.save()
        return super().form_valid(form)
