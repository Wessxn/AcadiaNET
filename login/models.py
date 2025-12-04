from django.db import models
from django.contrib.auth.models import AbstractUser, User
import uuid
from django.utils import timezone
from django.conf import settings

# Create your models here.
class Profile(AbstractUser):
    REQUIRED_FIELDS = ['email', 'first_name', 'last_name', 'major']
    email = models.EmailField(unique=False)
    major = models.CharField(max_length=50, blank=True)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']
    
# class Post(models.Model):
#     id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
#     author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
#     content = models.TextField()
#     created_at = models.DateTimeField(auto_now_add=True)

#     def publish(self):
#         self.created_at = timezone.now()
#         self.save()