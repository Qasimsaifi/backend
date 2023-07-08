from django.db import models
from django.contrib.auth.models import AbstractUser
from cloudinary.models import CloudinaryField
import uuid
from .manager import UserManager

def generate_unique_username():
    return str(uuid.uuid4())

class User(AbstractUser):
    username = models.CharField(
        max_length=240,
        default=generate_unique_username,
        unique=True,
    )
    email = models.EmailField(unique=True)
    mobile = models.CharField(max_length=14)
    profile_picture = CloudinaryField("image", blank=True, null=True)
    email_token = models.CharField(max_length=100, null=True, blank=True)
    forget_password = models.CharField(max_length=100, null=True, blank=True)
    last_login_time = models.DateTimeField(null=True, blank=True)
    last_logout_time = models.DateTimeField(null=True, blank=True)
    reset_password_token = models.CharField(max_length=100, null=True, blank=True)  # Add this field

    def __str__(self):
        return self.email

    objects = UserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []


