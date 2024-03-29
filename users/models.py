from django.contrib.auth.models import AbstractUser
from django.db import models
import uuid

from users.managers import UserManager

class User(AbstractUser):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False,unique=True)
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    updated_at = models.DateTimeField(auto_now=True)
    
    username = None

    objects = UserManager()

    USERNAME_FIELD: str = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name'] 