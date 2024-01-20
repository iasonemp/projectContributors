from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    age = models.PositiveIntegerField()
    country = models.CharField(max_length=100)
    residence = models.CharField(max_length=100)
    username = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.username

