from django.db import models
from django.contrib.auth.models import AbstractUser, User
import uuid
from django.utils import timezone
from django.conf import settings

# Create your models here.
class Profile(AbstractUser):
    email = models.EmailField(unique=False)
    major = models.CharField(max_length=50, blank=True)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    def save(self, *args, **kwargs):
          self.set_password(self.password)
          super().save(*args, **kwargs)