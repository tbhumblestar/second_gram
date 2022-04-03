from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    website_url = models.URLField(blank=True, max_length=200)
    bio = models.TextField(blank=True)
    phone_number = models.DecimalField(blank=True,max_digits=12,decimal_places=0)
