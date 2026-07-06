from django.db import models

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
        verbos_name = "Blog Category"
        verbos_name_plural = "Blog Categories"
        ordering = ["name"]

    def __str__(self):
        return self.name
    

class BlogPost(models.Model):
    title = models.CharField(max_length=1000)
    slug = models.CharField(max_length=250, unique=True, blank=True)

    category = models.ForeignKey(BlogCategory, on_delete=models.SET_NULL, null=True, blank=True, related_name="posts" )
    