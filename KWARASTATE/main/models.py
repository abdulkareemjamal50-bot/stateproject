from django.db import models
from django.utils.text import slugify

# Create your models here.
class ContactMessage(models.Model):
    full_name =models.CharField(max_length=50)
    email = models.EmailField()
    phone_no = models.CharField()
    service_of_interest =models.CharField()
    message = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.full_name


class BlogCategory(models.Model):
    name= models.CharField(max_length=50, unique=True)


    class Meta:
        verbose_name = "Blog Category"
        verbose_name_plural = "Blog Categories"
        ordering = ["name"]

    def __str__(self):
        return self.name
    

class BlogPost(models.Model):
    title = models.CharField(max_length=1000)
    slug = models.SlugField(max_length=250, unique=True, blank=True)

    category = models.ForeignKey(BlogCategory, on_delete=models.SET_NULL, null=True, blank=True, related_name="posts" )

    feature_image = models.ImageField(upload_to="blog/", blank=True, null=True)
    
    content= models.TextField()

    published_date = models.DateField()

    is_published = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    class Meta:
        ordering = ["-published_date"]
        verbose_name = "Blog Post"
        verbose_name_plural = "Blog Posts"

    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug =slugify(self.title)
            super().save(*args, **kwargs)

