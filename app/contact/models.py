from django.db import models


# Create your models here.

class ContactMe(models.Model):
    full_name = models.CharField(max_length=20 , verbose_name="Name")
    email = models.EmailField(max_length=40 , verbose_name="Email")
    message = models.TextField(verbose_name="Message")
    ip_address = models.GenericIPAddressField()
    user_agent = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f" fullname:{self.full_name} email:{self.email} message:{self.message}"
