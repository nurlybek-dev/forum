from django.urls import reverse_lazy
from django.views.generic.edit import FormView
from django.views.generic import DetailView, UpdateView

from .models import User
from .forms import EditProfileForm, UserCreationForm


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


class EditProfileView(UpdateView):
    model = User
    form_class = EditProfileForm
    template_name = 'users/edit_profile.html'
    context_object_name = 'profile'

    def form_valid(self, form: EditProfileForm):
        form.save()
        return super().form_valid(form)

    def get_success_url(self) -> str:
        return reverse_lazy('accounts:profile', kwargs={'pk': self.kwargs['pk']})
