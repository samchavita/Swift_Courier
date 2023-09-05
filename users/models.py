from django.db import models
import uuid

from django.contrib.auth.models import User

# Customer models
class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    customer_id = models.UUIDField(default=uuid.uuid4, primary_key=True, unique=True, editable=False)
    date_joined = models.DateTimeField(auto_now_add=True)
    first_name = models.CharField(max_length=50, null=True, blank=True)
    last_name = models.CharField(max_length=50, null=True, blank=True)
    username = models.CharField(max_length=50, null=True, blank=True)
    email = models.EmailField(max_length=255, null=True, blank=True)
    phone_number = models.CharField(max_length=15, null=True, blank=True)
    address = models.CharField(max_length=255, null=True, blank=True)
    profile_image = models.ImageField(upload_to='profiles/customer/', null=True, blank=True)

    def __str__(self):
        return str(self.username)
