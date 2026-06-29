from django.contrib import admin
from.models import ContactMessage

# Register your models here.
@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display=("full_name","email","phone_no","service_of_interest","created_at")