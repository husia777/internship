from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    subscribe_to_the_newsletter = models.BooleanField(default=False)
