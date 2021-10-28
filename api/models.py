from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    pass


class Message(models.Model):
    text = models.CharField(blank=False, max_length=300)
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=False)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)