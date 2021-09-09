from django.urls import path
from users.views import ProfileView, SignupView


urlpatterns = [
    path("signup/", SignupView.as_view(), name="signup"),
    path("profile/<int:pk>/", ProfileView.as_view(), name="profile")
]
