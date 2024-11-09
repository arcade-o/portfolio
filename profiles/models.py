from django.db import models
from django.contrib.auth.models import AbstractBaseUser,PermissionsMixin
from datetime import datetime
from .managers import ProfileManager

# Create your models here.

class project(models.Model):
    name = models.TextField(max_length=100)
    github = models.URLField()
    hidden = models.BooleanField(default=False)
    username = models.TextField()

    def __str__(self):
        return self.name

class profile(AbstractBaseUser,PermissionsMixin):
    username = models.TextField(max_length=100)
    email = models.EmailField(unique=True)
    github = models.URLField()
    projects = models.ForeignKey(project,on_delete = models.CASCADE, null=True)
    


    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    date_joined = models.DateTimeField(default=datetime.now)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = ProfileManager()

    def __str__(self):
        return self.email
