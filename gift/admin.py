from django.contrib import admin
from .models import Gift

@admin.register(Gift)
class AdminGift(admin.ModelAdmin):
    search_fields = ['name']