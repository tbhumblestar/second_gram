from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    website_url = models.URLField(blank=True, max_length=200)
    bio = models.TextField(blank=True)
    only_for_testing = models.TextField(blank=True)

