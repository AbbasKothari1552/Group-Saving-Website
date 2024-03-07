from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth import get_user_model
from .manager import userManager

user = get_user_model

from django.utils import timezone



class User(AbstractUser):

    username = None
    email = models.EmailField(unique = True)
    Name = models.CharField(max_length = 100, blank=False)
    phone_no = models.CharField(max_length = 100, unique = True)
    birth_date = models.DateField(blank=True, null=True)
    registration_date = models.DateTimeField(default=timezone.now)
    user_profile_image = models.ImageField(upload_to="profile",null=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    objects = userManager()
