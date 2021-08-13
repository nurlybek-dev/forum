from django.contrib import admin
from django.contrib.auth import admin as auth_admin

from .forms import UserCreationForm, UserChangeForm
from .models import User


class UserAdmin(auth_admin.UserAdmin):
    add_form = UserCreationForm
    form = UserChangeForm
    model = User
    list_display = ['username', 'email', 'is_staff', 'is_active']
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'password1', 'password2', 'is_staff', 'is_active')}
        ),
    )
    search_fields = ('username', 'email',)
    ordering = ('username', 'email',)


admin.site.register(User, UserAdmin)
