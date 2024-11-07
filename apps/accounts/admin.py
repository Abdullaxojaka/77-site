from django.contrib import admin
from .models import User
from django.contrib.auth.admin import Admin

@admin.register(User)
class CustomUserAdmin(Admin):
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Shaxsiy ma\'lumotlar', {'fields': ('first_name', 'last_name', 'email', 'phone_number', 'bio', 'profile_image')}),
        ('Ruxsatlar', {'fields': ('is_active', 'is_staff', 'is_superuser')}),
        ('Muhim sanalar', {'fields': ('last_login', 'date_joined')}),
    )
