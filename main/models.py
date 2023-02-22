from django.contrib.auth.models import AbstractUser
from django.db import models
from urllib.parse import urlparse


class Headers(models.Model):
    title = models.CharField(max_length=60)
    url = models.URLField(max_length=255, default='http://127.0.0.1:8000/home/')

    def url_text(self):
        parsed_url = urlparse(self.url)
        return parsed_url.hostname.replace("www.", "") + "/..."


class User(AbstractUser):
    subscribe_to_the_newsletter = models.BooleanField(default=False)
