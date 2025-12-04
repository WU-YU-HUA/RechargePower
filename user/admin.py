from django.contrib import admin
from .models import User

@admin.register(User)
class AdminUser(admin.ModelAdmin):
    search_fields = ['username']