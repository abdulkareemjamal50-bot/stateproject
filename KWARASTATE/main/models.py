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
    