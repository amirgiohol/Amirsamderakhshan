from django.contrib import admin
from .models import ContactMe

@admin.register(ContactMe)
class ContactMeAdmin(admin.ModelAdmin):
    list_display = ("full_name","email","created_at")
