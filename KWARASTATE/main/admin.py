from django.contrib import admin
from.models import ContactMessage, BlogCategory, BlogPost

# Register your models here.
@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display=("full_name","email","phone_no","service_of_interest","created_at")


@admin.register(BlogCategory)
class BlogCategoryAdmin(admin.ModelAdmin):
    list_display=("name",)


@admin.register( BlogPost)
class  BlogPostAdmin(admin.ModelAdmin):
    list_display=("title","category","published_date","is_published","created_at")
    list_filter= ("category","published_date", "is_published") 
    search_fields=("title","content")
    list_editable=("is_published",)
    ordering=("-published_date",)
    date_hierarchy=("published_date")
                    
    prepopulated_fields ={
        "slug":("title",)
    }