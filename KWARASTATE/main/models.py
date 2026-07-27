from django.db import models
from django.utils.text import slugify

class ContactMessage(models.Model):
    full_name = models.CharField(max_length=50)
    email = models.EmailField()
    phone_no = models.CharField(max_length=20)  # Fixed: Added max_length
    service_of_interest = models.CharField(max_length=100)  # Fixed: Added max_length
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.full_name


class BlogCategory(models.Model):
    name = models.CharField(max_length=50, unique=True)

    class Meta:
        verbose_name = "Blog Category"
        verbose_name_plural = "Blog Categories"
        ordering = ["name"]

    def __str__(self):
        return self.name
    

class BlogPost(models.Model):
    title = models.CharField(max_length=250)  # Adjusted: Aligned with slug max_length
    slug = models.SlugField(max_length=250, unique=True, blank=True)
    category = models.ForeignKey(
        BlogCategory, 
        on_delete=models.SET_NULL, 
        null=True, 
        blank=True, 
        related_name="posts"
    )
    featured_image = models.ImageField(upload_to="media/blog/", blank=True, null=True)
    content = models.TextField()
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
        # Auto-generate unique slug if it doesn't exist
        if not self.slug:
            base_slug = slugify(self.title)[:240]  # Truncate slightly to leave room for suffix
            slug = base_slug
            counter = 1
            
            # Loop to ensure the slug is completely unique in the database
            while BlogPost.objects.filter(slug=slug).exists():
                slug = f"{base_slug}-{counter}"
                counter += 1
                
            self.slug = slug

        # Fixed: Moved out of the 'if' block so existing records can update successfully
        super().save(*args, **kwargs)

class Testimonial(models.Model):
            name =models.CharField(max_length=50)
            role=models.CharField(max_length=50)
            message =models.TextField()
            image=models.ImageField(upload_to='media/testimonials/' , blank="True", null="True")
            ratings=models.IntegerField(default=5)
            is_active = models.BooleanField(default=True)
            created_at = models.DateTimeField(auto_now_add=True)


            def __str__(self):
                return self.name
            
            

