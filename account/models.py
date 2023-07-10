from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Profile(models.Model):
    active = models.BooleanField(default=False)
    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True, null=True)
    number = models.CharField(max_length=100, blank=True, null=True)
    
