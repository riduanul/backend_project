from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class CustomUser(AbstractUser):

    ROLE=[
        ('admin', 'Admin'),
        ('user', 'User'),
    ]

    role = models.CharField(max_length=50, choices=ROLE, default='user')

    


